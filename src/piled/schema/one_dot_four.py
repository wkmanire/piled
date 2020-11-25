from enum import Enum, auto
from typing import List, Union

from attr import attrs, attrib


class MapOrientation(Enum):
    orthogonal = auto()
    isometric = auto()
    staggered = auto()
    hexagonal = auto()


class RenderOrder(Enum):
    right_down = auto()
    right_up = auto()
    left_down = auto()
    left_up = auto()


class Axis(Enum):
    x = auto()
    y = auto()


class StaggerIndex(Enum):
    even = auto()
    odd = auto()


@attrs
class ARGBColor:
    alpha: int = attrib()
    red: int = attrib()
    green: int = attrib()
    blue: int = attrib()

    def __str__(self) -> str:
        return f"#{self.alpha:02X}{self.red:02X}{self.green:02X}{self.blue:02X}"


@attrs
class RGBColor:
    red: int = attrib()
    green: int = attrib()
    blue: int = attrib()

    def __str__(self) -> str:
        return f"#{self.red:02X}{self.green:02X}{self.blue:02X}"


Color = Union[ARGBColor, RGBColor]


class PropertyType(Enum):
    string = auto()
    int = auto()
    float = auto()
    bool = auto()
    color = auto()
    file = auto()
    object = auto()


@attrs
class Property:
    name: str = attrib()
    property_type: PropertyType = attrib()
    value: str = attrib()


class GridOrientation(Enum):
    orthogonal = auto()
    isometric = auto()


@attrs
class Grid:
    height: int = attrib()
    orientation: GridOrientation = attrib()
    width: int = attrib()


class ObjectAlignment(Enum):
    unspecified = auto()
    top_left = auto()
    top = auto()
    top_right = auto()
    left = auto()
    center = auto()
    right = auto()
    bottom_left = auto()
    bottom = auto()
    bottom_right = auto()


@attrs
class Terrain:
    name: str = attrib()
    properties: List[Property] = attrib()
    tile: int = attrib()


@attrs
class TileOffset:
    x: int = attrib()
    y: int = attrib()


@attrs
class Frame:
    duration: int = attrib()
    tile_id: int = attrib()


@attrs
class WangColor:
    color: Color = attrib()
    name: str = attrib()
    probability: float = attrib()
    tile: int = attrib()


@attrs
class WangTile:
    d_flip: bool = attrib()
    h_flip: bool = attrib()
    tile_id: int = attrib()
    v_flip: bool = attrib()
    wang_id: List[bytearray] = attrib()


@attrs
class WangSet:
    corner_colors: List[WangColor] = attrib()
    edge_colors: List[WangColor] = attrib()
    name: str = attrib()
    properties: List[Property] = attrib()
    tile: int = attrib()
    wang_tiles: List[WangTile] = attrib()


@attrs
class Tile:
    animation: List[Frame] = attrib()
    id: int = attrib()
    image: str = attrib()
    image_height: str = attrib()
    image_width: str = attrib()
    object_group: "Layer" = attrib()
    probability: float = attrib()
    properties: List[Property] = attrib()
    terrain: List[Terrain] = attrib()
    type: str = attrib()


@attrs
class Tileset:
    background_color: Color = attrib()
    columns: int = attrib()
    first_gid: int = attrib()
    grid: Grid = attrib()
    image: str = attrib()
    image_height: int = attrib()
    image_width: int = attrib()
    margin: int = attrib()
    name: str = attrib()
    object_alignment: ObjectAlignment = attrib()
    properties: List[Property] = attrib()
    source: str = attrib()
    spacing: int = attrib()
    terrains: List[Terrain] = attrib()
    tile_count: int = attrib()
    tiled_version: str = attrib()
    tile_height: int = attrib()
    tile_offset: TileOffset = attrib()
    tiles: List[Tile] = attrib()
    tile_width: int = attrib()
    transparent_color: RGBColor = attrib()
    type: str = attrib()
    version: int = attrib()
    wang_sets: List[WangSet] = attrib()


@attrs
class Chunk:
    data: Union[List[int], str] = attrib()
    height: int = attrib()
    width: int = attrib()
    x: int = attrib()
    y: int = attrib()


class Compression(Enum):
    zlib = auto()
    gzip = auto()
    zstd = auto()


class DrawOrder(Enum):
    top_down = auto()
    index = auto()


class Encoding(Enum):
    csv = auto()
    base_64 = auto()


@attrs
class Point:
    x: float = attrib()
    y: float = attrib()


class HorizontalAlignment(Enum):
    center = auto()
    right = auto()
    justify = auto()
    left = auto()


class VerticalAlignment(Enum):
    center = auto()
    bottom = auto()
    top = auto()


@attrs
class Text:
    bold: bool = attrib()
    color: Color = attrib()
    font_family: str = attrib()
    h_align: HorizontalAlignment = attrib()
    italic: bool = attrib()
    kerning: bool = attrib()
    pixel_size: int = attrib()
    strike_out: bool = attrib()
    text: "Text" = attrib()
    underline: bool = attrib()
    v_align: VerticalAlignment = attrib()
    wrap: bool = attrib()


@attrs
class Object:
    ellipse: bool = attrib()
    gid: int = attrib()
    height: float = attrib()
    id: int = attrib()
    name: str = attrib()
    point: bool = attrib()
    polygon: List[Point] = attrib()
    polyline: List[Point] = attrib()
    properties: List[Property] = attrib()
    rotation: float = attrib()
    template: str = attrib()
    text: Text = attrib()
    type: str = attrib()
    visible: bool = attrib()
    x: int = attrib()
    y: int = attrib()


class LayerType(Enum):
    tile_layer = auto()
    object_group = auto()
    image_layer = auto()
    group = auto()


@attrs
class Layer:
    chunks: List[Chunk] = attrib()
    compression: Compression = attrib()
    data: Union[List[int], bytes] = attrib()
    draw_order: DrawOrder = attrib()
    encoding: Encoding = attrib()
    height: int = attrib()
    id: int = attrib()
    image: str = attrib()
    layers: List["Layer"] = attrib()
    name: str = attrib()
    objects: List[Object] = attrib()
    offset_x: float = attrib()
    offset_y: float = attrib()
    opacity: float = attrib()
    properties: List[Property] = attrib()
    start_x: int = attrib()
    start_y: int = attrib()
    tint_color: str = attrib()
    transparent_color: str = attrib()
    type: LayerType = attrib()
    visible: bool = attrib()
    width: int = attrib()
    x: int = attrib()
    y: int = attrib()


@attrs
class Map:
    background_color: ARGBColor = attrib()
    compression_level: int = attrib()
    height: int = attrib()
    hex_side_length: int = attrib()
    infinite: bool = attrib()
    layers: List[Layer] = attrib()
    next_layer_id: int = attrib()
    next_object_id: int = attrib()
    orientation: MapOrientation = attrib()
    properties: List[Property] = attrib()
    render_order: RenderOrder = attrib()
    stagger_axis: Axis = attrib()
    stagger_index: StaggerIndex = attrib()
    tiled_version: str = attrib()
    tiled_width: int = attrib()
    tilesets: List[Tileset] = attrib()
    tile_height: int = attrib()
    version: str = attrib()
    width: int = attrib()
