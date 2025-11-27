from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Dataset:
    """
    Immutable container for loaded dataset(s) with consistent interface.

    This wrapper eliminates the Union[Any, Dict[str, Any]] type instability by
    providing a single, predictable return type from all data loading operations.

    A Dataset always wraps data as a dictionary (single datasets use a default key),
    making the API consistent and type-safe.

    Attributes:
        data (Dict[str, Any]): Dictionary mapping table names to data objects.
            For single-table datasets, uses the default key "data".
            For multi-table datasets, keys are defined in the config.

    Example:
        Single-table dataset (loaded internally):
            Dataset(data={"data": pd.DataFrame(...)})

        Multi-table dataset:
            Dataset(data={"train": pd.DataFrame(...), "test": pd.DataFrame(...)})

        Access:
            dataset.data["data"]  # Single table
            dataset.data["train"]  # First table from multi-table
    """

    data: Dict[str, Any] = field(default_factory=dict)

    def __getitem__(self, key: str) -> Any:
        """
        Convenient access to individual tables within the dataset.

        Args:
            key (str): Table name (e.g., "data", "train", "test").

        Returns:
            Any: The requested data object.

        Raises:
            KeyError: If the table name doesn't exist.

        Example:
            dataset["data"]
            dataset["train"]
        """
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value

    def __contains__(self, key: str) -> bool:
        """Check if a table exists in the dataset."""
        return key in self.data

    def keys(self):
        """Get all table names in this dataset."""
        return self.data.keys()

    def items(self):
        """Iterate over (table_name, data) pairs."""
        return self.data.items()

    def __len__(self) -> int:
        """Return the number of tables in this dataset."""
        return len(self.data)

    def __repr__(self) -> str:
        """Return a clear representation of the dataset structure."""
        tables = ", ".join(self.data.keys())
        return f"Dataset(tables=[{tables}])"
