# 基于Dask的分布式数据清洗
import dask.dataframe as dd

def anonymize_dataset(path):
    ddf = dd.read_parquet(path)
    return ddf.map_partitions(
        lambda df: df.apply(anonymizer.process, axis=1),
        meta=df.dtypes
    ).compute(scheduler='threads')
