import dash_bootstrap_components as dbc
from dash import html

button_groups = html.Div(
    [
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="lg",
            class_name="me-1",
        ),
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="md",
            class_name="me-1",
        ),
        dbc.ButtonGroup(
            [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
            size="sm",
        ),
    ]
)
