from pathlib import Path
from datetime import datetime, timezone
import hashlib
import uuid

import pandas as pd


# project paths using .resolve to get absolute path, and .parent to get parent directory
project_root = Path(__file__).resolve().parent.parent

source_file = (
    project_root
    / "data"
    / "silver"
    / "power_query_etl.xlsx"
)

dq_source_sheet = "dq_all_results"
transaction_source_sheet = "transformed_data"

output_dir = project_root / "data" / "monitoring"

# historical dq rule-level results
dq_history_file = output_dir / "dq_run_history.csv"

# historical full transaction results
transaction_history_file = output_dir / "transaction_history.csv"

# historical transaction run-level metadata
transaction_run_history_file = output_dir / "transaction_run_history.csv"


def generate_dataset_fingerprint(dataframe):
    # create a stable hash from the current transformed dataset
    dataframe_hash = pd.util.hash_pandas_object(
        dataframe,
        index=False
    ).values.tobytes()

    return hashlib.sha256(dataframe_hash).hexdigest()


def main():
    # create monitoring directory if it does not exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # read current dq results
    dq_results = pd.read_excel(
        source_file,
        sheet_name=dq_source_sheet
    )

    # read current transformed transaction data
    transaction_data = pd.read_excel(
        source_file,
        sheet_name=transaction_source_sheet
    )

    # generate metadata for this execution
    run_timestamp = datetime.now(timezone.utc)
    run_id = (
        f"dq_{run_timestamp:%Y%m%dT%H%M%SZ}_"
        f"{uuid.uuid4().hex[:8]}"
    )

    # generate fingerprint before adding run metadata
    dataset_fingerprint = generate_dataset_fingerprint(
        transaction_data
    )

    # add execution metadata to dq results
    dq_results.insert(0, "run_id", run_id)
    dq_results.insert(
        1,
        "run_timestamp",
        run_timestamp.isoformat()
    )

    # append dq rule-level results to historical repository
    if dq_history_file.exists():
        dq_results.to_csv(
            dq_history_file,
            mode="a",
            header=False,
            index=False
        )
    else:
        dq_results.to_csv(
            dq_history_file,
            index=False
        )

    # check whether the current dataset has already been processed
    dataset_already_processed = False

    if transaction_run_history_file.exists():
        transaction_run_history = pd.read_csv(
            transaction_run_history_file
        )

        if "dataset_fingerprint" in transaction_run_history.columns:
            dataset_already_processed = (
                transaction_run_history[
                    "dataset_fingerprint"
                ] == dataset_fingerprint
            ).any()

    # append transaction data only if the dataset is new
    if not dataset_already_processed:
        # add execution metadata to transformed transaction data
        transaction_data.insert(0, "run_id", run_id)
        transaction_data.insert(
            1,
            "run_timestamp",
            run_timestamp.isoformat()
        )

        # append full transformed transaction data to historical repository
        if transaction_history_file.exists():
            transaction_data.to_csv(
                transaction_history_file,
                mode="a",
                header=False,
                index=False
            )
        else:
            transaction_data.to_csv(
                transaction_history_file,
                index=False
            )

        transaction_history_status = "appended"

    else:
        transaction_history_status = "skipped_duplicate"

    # create one transaction run-level metadata record
    transaction_run_history = pd.DataFrame(
        [{
            "run_id": run_id,
            "run_timestamp": run_timestamp.isoformat(),
            "dataset_fingerprint": dataset_fingerprint,
            "total_transactions": len(transaction_data),
            "transaction_history_status": transaction_history_status
        }]
    )

    # append transaction run-level metadata to historical repository
    if transaction_run_history_file.exists():
        transaction_run_history.to_csv(
            transaction_run_history_file,
            mode="a",
            header=False,
            index=False
        )
    else:
        transaction_run_history.to_csv(
            transaction_run_history_file,
            index=False
        )

    # display execution results
    print("historical logging completed successfully")
    print(f"run_id: {run_id}")
    print(f"dq records logged: {len(dq_results)}")
    print(f"total transactions: {len(transaction_data)}")
    print(f"dataset fingerprint: {dataset_fingerprint}")
    print(
        f"transaction history status: "
        f"{transaction_history_status}"
    )
    print(f"dq output: {dq_history_file}")
    print(f"transaction output: {transaction_history_file}")
    print(
        f"transaction run output: "
        f"{transaction_run_history_file}"
    )


if __name__ == "__main__":
    main()