## Notes on Python version of a React project

For examples, refer to https://github.com/markfinger/python-react.

Library `python-react` uses Python 3 and has `requirements.txt` — Flask is needed for the examples, with Django optional.

### Server-side rendering

The example code uses a Node-based "render server", `render_server.js` (dependency file `package.json`), which handles all (or some?) calls to `render`. An example of a Python-based render server from MediaWiki is [nserver.py](https://github.com/pediapress/mwlib/blob/master/mwlib/nserve.py) for examination. 

```bash
```

The [Redux](https://github.com/reactjs/redux/blob/master/docs/recipes/ServerRendering.md) site says:

> The most common use case for server-side rendering is to handle the _initial_ render when a user (or search engine crawler) first requests our app. When the server receives the request, it renders the required component(s) into an HTML string, and then sends it as a response to the client. From that point on, the client takes over rendering duties.

[end]