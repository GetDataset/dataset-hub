from dataclasses import dataclass, field
from typing import Dict, Generic, ItemsView, KeysView, TypeVar

DataLikeT = TypeVar("DataLikeT")
"""
Type variable representing the data stored inside a Dataset.
In real cases it may be e.x. pd.DataFrame, tf.Dataset, 
networX.Graph, etc..
"""


@dataclass
class Dataset(Generic[DataLikeT]):
    """
    Generic dataset container.

    Type parameters:
        DataT: The type of each data object stored under names.

    Attributes:
        data (Dict[str, DataLikeT]): Dictionary mapping table names to data objects

    Example:
        Creating:
            from dataset_hub._core.dataset import Dataset
            import pandas as pd
            df = pd.DataFrame({"a":[1]})
            dataset: Dataset[pd.DataFrame] = Dataset()
            dataset["data"] = df

        Access:
            df = dataset.data["data"]
    """

    data: Dict[str, DataLikeT] = field(default_factory=dict)

    def __getitem__(self, key: str) -> DataLikeT:
        """
        Convenient access to individual tables within the dataset.

        Args:
            key (str): Table name (e.g., "data", "train", "test").

        Returns:
            DataLike: The requested data object.

        Raises:
            KeyError: If the table name doesn't exist.

        Example:
            dataset["data"]
            dataset["train"]
        """
        return self.data[key]

    def __setitem__(self, key: str, value: DataLikeT) -> None:
        self.data[key] = value

    def __contains__(self, key: str) -> bool:
        """Check if a table exists in the dataset."""
        return key in self.data

    def keys(self) -> KeysView[str]:
        """Get all table names in this dataset."""
        return self.data.keys()

    def items(self) -> ItemsView[str, DataLikeT]:
        """Iterate over (table_name, data) pairs."""
        return self.data.items()

    def __len__(self) -> int:
        """Return the number of tables in this dataset."""
        return len(self.data)

    def __repr__(self) -> str:
        """Return a clear representation of the dataset structure."""
        tables = ", ".join(self.data.keys())
        return f"Dataset(tables=[{tables}])"
