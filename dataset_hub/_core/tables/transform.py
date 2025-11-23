from typing import Dict, Any
def transform_tables(tables: Dict[str, Any]) -> Dict[str, Any]:
    for table_name, table in tables.items():
        tables[table_name] = transform_table(table)
    return tables

def transform_table(table: Any) -> Any:
    return table