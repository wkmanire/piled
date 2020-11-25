from piled.schema.one_dot_four import ARGBColor


def test_color_str():
    c: ARGBColor = ARGBColor(255, 255, 255, 255)
    assert str(c) == "#FFFFFFFF"
