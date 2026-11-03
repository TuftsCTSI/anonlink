"""Types for typechecking. Aimed at Mypy."""

import array as _array
import typing as _typing

# This is for parametrisation only. You shouldn't need to import it.
Record = _typing.TypeVar('Record')

Dataset = _typing.Sequence[Record]

if _typing.TYPE_CHECKING:
    FloatArrayType = _array.array[float]
    IntArrayType = _array.array[int]
    CharArrayType = _array.array[int]
else:
    FloatArrayType = _array.array
    IntArrayType = _array.array
    CharArrayType = _array.array

CandidatePairs = _typing.Tuple[FloatArrayType,
                       _typing.Tuple[IntArrayType, ...],
                       _typing.Tuple[IntArrayType, ...]]

BlockingFunction = _typing.Callable[
    [int, int, Record],
    _typing.Iterable[_typing.Hashable]]

class SimilarityFunction(_typing.Protocol):
    def __call__(
        self,
        datasets: _typing.Sequence[Dataset],
        threshold: float,
        /,
        *,
        k: _typing.Optional[int] = None
    ) -> _typing.Tuple[FloatArrayType, _typing.Sequence[IntArrayType]]:
        ...

DatasetChunkInfo = _typing.TypedDict(
    'DatasetChunkInfo',
    {'datasetIndex': int,
     'range': _typing.List[int]})
ChunkInfo = _typing.List[DatasetChunkInfo]

DatasetAndRecordIndex = _typing.Tuple[int, int]
MatchGroups = _typing.Sequence[_typing.Sequence[DatasetAndRecordIndex]]
