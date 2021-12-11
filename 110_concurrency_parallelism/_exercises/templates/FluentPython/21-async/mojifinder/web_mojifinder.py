____ pathlib ______ Path
____ unicodedata ______ name

____ fastapi ______ FastAPI
____ fastapi.responses ______ HTMLResponse
____ pydantic ______ BaseModel

____ charindex ______ InvertedIndex

STATIC_PATH = Path(__file__).parent.absolute() / 'static'  # <1>

app = FastAPI(  # <2>
    title='Mojifinder Web',
    description='Search for Unicode characters by name.',
)

c_ CharName(BaseModel):  # <3>
    char: s..
    name: s..

___ init(app):  # <4>
    app.state.index = InvertedIndex()
    app.state.form = (STATIC_PATH / 'form.html').read_text()

init(app)  # <5>

@app.get('/search', response_model=list[CharName])  # <6>
@ ___ search(q: s..):  # <7>
    chars = sorted(app.state.index.search(q))
    r_ ({'char': c, 'name': name(c)} ___ c __ chars)  # <8>

@app.get('/', response_class=HTMLResponse, include_in_schema=F..)
___ form():  # <9>
    r_ app.state.form

# no main funcion  # <10>