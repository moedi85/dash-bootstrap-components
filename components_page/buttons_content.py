from pathlib import Path

import dash_html_components as html

from .api_doc import ApiDoc
from .components.buttons.group import buttons as buttons_group
from .components.buttons.outline import buttons as buttons_outline
from .components.buttons.simple import buttons as buttons_simple
from .helpers import (
    ExampleContainer,
    HighlightedSource,
    load_source_with_environment,
)
from .metadata import get_component_metadata

HERE = Path(__file__).parent
BUTTONS = HERE / "components" / "buttons"

buttons_simple_source = (BUTTONS / "simple.py").read_text()
buttons_usage_source = (BUTTONS / "usage.py").read_text()
buttons_outline_source = (BUTTONS / "outline.py").read_text()
buttons_group_source = (BUTTONS / "group.py").read_text()


def get_content(app):
    return [
        html.H2("Buttons"),
        ExampleContainer(buttons_simple),
        HighlightedSource(buttons_simple_source),
        html.H4("Using buttons"),
        ExampleContainer(
            load_source_with_environment(
                buttons_usage_source, "button", {"app": app}
            )
        ),
        HighlightedSource(buttons_usage_source),
        html.H4("Outline buttons"),
        ExampleContainer(buttons_outline),
        HighlightedSource(buttons_outline_source),
        html.H4("Button group"),
        ExampleContainer(buttons_group),
        HighlightedSource(buttons_group_source),
        ApiDoc(get_component_metadata("src/components/Button.js")),
    ]
