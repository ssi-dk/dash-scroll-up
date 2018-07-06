import dash_scroll_up
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    dash_scroll_up.DashScrollUp(
        id='input',
        label='my-label'
    ),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum"),
    html.P("Lorem ipsum")
])


if __name__ == '__main__':
    app.run_server(debug=True)
