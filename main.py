from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="The Grand Voyage — A One Piece Fan Adventure")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ── Crew Data ────────────────────────────────────────────────────────────────
CREW = [
    {
        "name": "Monkey D. Luffy",
        "role": "Captain",
        "epithet": "Straw Hat",
        "bounty": "3,000,000,000",
        "description": "Ate a rubber fruit, somehow became the world's most wanted man. Still can't swim. Still went to sea. Peak logic.",
        "image": "https://i.pinimg.com/736x/61/4b/69/614b696ee731f7b96c3181144585d87d.jpg",
        "flag_color": "#E63946",
        "specialty": "Being impossibly lucky",
    },
    {
        "name": "Roronoa Zoro",
        "role": "First Mate",
        "epithet": "Pirate Hunter",
        "bounty": "1,111,000,000",
        "description": "Three swords. One man. Zero sense of direction. Once got lost going from the kitchen to the bathroom.",
        "image": "https://i.pinimg.com/736x/5f/2d/63/5f2d63c61799642cb81b6f5cf14c9076.jpg",
        "flag_color": "#2D6A4F",
        "specialty": "Sleeping at inappropriate times",
    },
    {
        "name": "Nami",
        "role": "Navigator",
        "epithet": "Cat Burglar",
        "bounty": "366,000,000",
        "description": "Charges 100,000 berries to borrow a pen. Somehow everyone is okay with this. Also knows exactly where we are.",
        "image": "https://i.pinimg.com/1200x/ba/f1/cc/baf1cc280bc69b16b8171ac594171805.jpg",
        "flag_color": "#F4A261",
        "specialty": "Weather manipulation & financial domination",
    },
    {
        "name": "Usopp",
        "role": "Sniper",
        "epithet": "God",
        "bounty": "500,000,000",
        "description": "Has 8000 followers, can hit targets from 4km, and once defeated a giant. But don't tell him we found out.",
        "image": "https://i.pinimg.com/1200x/22/ac/22/22ac22eb92c170f8b835cffaaa1ab3d3.jpg",
        "flag_color": "#8B5E3C",
        "specialty": "Lying so hard it becomes true",
    },
    {
        "name": "Sanji",
        "role": "Cook",
        "epithet": "Black Leg",
        "bounty": "1,032,000,000",
        "description": "Kicks at face level exclusively. Cries at beautiful sunsets and again when dinner is overcooked. Complex man.",
        "image": "https://i.pinimg.com/1200x/04/53/eb/0453ebf107bd57593f1fe9df75b29ac6.jpg",
        "flag_color": "#1D3557",
        "specialty": "Cooking & dramatic spinning kicks",
    },
    {
        "name": "Tony Tony Chopper",
        "role": "Doctor",
        "epithet": "Cotton Candy Lover",
        "bounty": "1,000",
        "description": "Has a 50-berri bounty because marines thought he was just a random tanuki. Most devastating insult ever.",
        "image": "https://i.pinimg.com/736x/3e/7b/ab/3e7bab50f225f4106b9c85da7405823f.jpg",
        "flag_color": "#E9C46A",
        "specialty": "Medical miracles & being adorable",
    },
    {
        "name": "Nico Robin",
        "role": "Archaeologist",
        "epithet": "Devil Child",
        "bounty": "930,000,000",
        "description": "Quiet, razor-brained archaeologist who reads the Poneglyphs and excavates dangerous secrets. Very well-read, will very calmly end you.",
        "image": "https://i.pinimg.com/736x/af/27/a7/af27a7114b616411f2f611bd17409b08.jpg",
        "flag_color": "#6A4C93",
        "specialty": "Archaeology & Hana Hana no Mi abilities",
    },
    {
        "name": "Franky",
        "role": "Shipwright",
        "epithet": "Cyborg",
        "bounty": "394,000,000",
        "description": "Loud, proud cyborg who built the Thousand Sunny. Drinks cola, builds weapons, and fixes whatever's broken (usually with style).",
        "image": "https://i.pinimg.com/1200x/64/15/d6/6415d633cc5e3f10450cf2f98dbafdb2.jpg",
        "flag_color": "#FF6F00",
        "specialty": "Shipbuilding, heavy weapons & cola-powered engineering",
    },
    {
        "name": "Brook",
        "role": "Musician",
        "epithet": "Soul King",
        "bounty": "383,000,000",
        "description": "A living skeleton with impeccable manners, fearsome swordsmanship, and a taste for eerie ballads.",
        "image": "https://i.pinimg.com/1200x/57/db/17/57db1746254f956866ad1f0cff9e7536.jpg",
        "flag_color": "#F3E9E1",
        "specialty": "Music, swordplay, and soul-based hijinks",
    },
    {
        "name": "Jinbei",
        "role": "Helmsman",
        "epithet": "Knight of the Sea",
        "bounty": "438,000,000",
        "description": "A calm and honorable fish-man, master of Fish-Man Karate and a steady hand at the wheel.",
        "image": "https://i.pinimg.com/736x/67/3f/6f/673f6f520cea631ba46221b128fcbb7a.jpg",
        "flag_color": "#0E6F6A",
        "specialty": "Fish-Man Karate & expert helmsmanship",
    },
]

# ── Wanted Posters ────────────────────────────────────────────────────────────
WANTED = [
    {
        "name": "Monkey D. Luffy",
        "epithet": "Straw Hat",
        "bounty": "3,000,000,000",
        "crime": "Wrecking entire governments, befriending giants, punching World Nobles, liberating nations, and eating all the meat.",
        "image": "https://i.pinimg.com/736x/61/4b/69/614b696ee731f7b96c3181144585d87d.jpg",
        "danger": "EXTREMELY",
    },
    {
        "name": "Roronoa Zoro",
        "epithet": "Pirate Hunter",
        "bounty": "1,111,000,000",
        "crime": "Cutting entire buildings in half, getting lost on perfectly straight roads, and sleeping through important battles.",
        "image": "https://i.pinimg.com/736x/5f/2d/63/5f2d63c61799642cb81b6f5cf14c9076.jpg",
        "danger": "EXTREMELY",
    },
    {
        "name": "Vinsmoke Sanji",
        "epithet": "Black Leg",
        "bounty": "1,032,000,000",
        "crime": "Kicking warships, feeding enemy soldiers, crying about food, and refusing to use his hands in a fight.",
        "image": "https://i.pinimg.com/1200x/04/53/eb/0453ebf107bd57593f1fe9df75b29ac6.jpg",
        "danger": "EXTREMELY",
    },
]

# ── Islands ───────────────────────────────────────────────────────────────────
ISLANDS = [
    {
        "id": "dawn-island",
        "name": "Dawn Island",
        "subtitle": "Where it all began",
        "lore": "A quiet East Blue island where a boy in a straw hat declared he'd be King of the Pirates. Bandits laughed. They were wrong.",
        "x": 12,
        "y": 65,
        "icon": "🏝️",
        "color": "#2DC653",
        "visited": True,
    },
    {
        "id": "arlong-park",
        "name": "Arlong Park",
        "subtitle": "Where fish men learned humility",
        "lore": "A fish-man ruled here for years. Then a rubber fist punched his throne into orbit. The sea smelled like justice that day.",
        "x": 22,
        "y": 58,
        "icon": "🐟",
        "color": "#0077B6",
        "visited": True,
    },
    {
        "id": "alabasta",
        "name": "Alabasta",
        "subtitle": "Desert kingdom. Giant crocodile problem.",
        "lore": "Sand, sun, and one Warlord playing both sides of a civil war. Also Vivi cried and everyone pretended not to notice.",
        "x": 38,
        "y": 45,
        "icon": "🏜️",
        "color": "#E9C46A",
        "visited": True,
    },
    {
        "id": "skypiea",
        "name": "Skypiea",
        "subtitle": "Sky island. Real. Yes, really.",
        "lore": "An island in the clouds ruled by a god with a golden stick. Luffy punched the god. He punched back. Luffy won. Standard.",
        "x": 55,
        "y": 30,
        "icon": "☁️",
        "color": "#AED9E0",
        "visited": True,
    },
    {
        "id": "water-seven",
        "name": "Water Seven",
        "subtitle": "City of water & betrayal",
        "lore": "A city built on water where shipwrights are gods. Robin left. The crew fell apart. Then they put it back together. Ugly cry moment.",
        "x": 68,
        "y": 50,
        "icon": "🚢",
        "color": "#457B9D",
        "visited": True,
    },
    {
        "id": "marineford",
        "name": "Marineford",
        "subtitle": "The war that broke everything",
        "lore": "Every marine, every Warlord, three Admirals, and a Yonko. Luffy brought one rubber fist and sheer willpower. It wasn't enough. Yet.",
        "x": 82,
        "y": 40,
        "icon": "⚓",
        "color": "#E63946",
        "visited": True,
    },
    {
        "id": "wano",
        "name": "Wano Kuni",
        "subtitle": "Samurai. Oni. Very dramatic.",
        "lore": "A closed nation, a dragon shogun, and enough swords to fill an ocean. Zoro finally felt at home. He still got lost twice.",
        "x": 72,
        "y": 72,
        "icon": "⛩️",
        "color": "#BC4749",
        "visited": True,
    },
    {
        "id": "laugh-tale",
        "name": "Laugh Tale",
        "subtitle": "The final island. Marked ???",
        "lore": "Nobody knows what's here. Roger laughed when he found it. The name says it all. One day, a straw hat will laugh there too.",
        "x": 90,
        "y": 20,
        "icon": "❓",
        "color": "#6A0572",
        "visited": False,
    },
]

# ── Adventure Log ─────────────────────────────────────────────────────────────
ADVENTURE_LOG = [
    {
        "date": "Year 1522",
        "title": "The Barrel That Changed Everything",
        "entry": "A boy named Luffy got himself sealed in a barrel to hide from pirates. The pirates opened the barrel. They became his crew. Somehow.",
        "location": "East Blue",
        "outcome": "victory",
        "weather": "Sunny, suspicious",
    },
    {
        "date": "Year 1524",
        "title": "We Fought a Giant Crocodile & His Desert Empire",
        "entry": "Baroque Works. Sand sand fruit. Fake drought. Real coup. Luffy died twice (arguably). Won anyway. Alabasta owes us forever.",
        "location": "Alabasta Kingdom",
        "outcome": "victory",
        "weather": "Sandstorm, then sunshine",
    },
    {
        "date": "Year 1525",
        "title": "Sky Island Was Real. Nobody Apologized.",
        "entry": "We sailed into the sky. Found an entire civilization. Punched their self-declared god. Left. Scientists still won't believe us.",
        "location": "Skypiea",
        "outcome": "victory",
        "weather": "Thunderous. Lightning. Dramatic.",
    },
    {
        "date": "Year 1527",
        "title": "Enies Lobby — The Day We Declared War on the World Government",
        "entry": "The crew almost quit. Then Luffy said four words: 'I want to fight.' We burned their flag. We stole Robin back. Worth it.",
        "location": "Enies Lobby",
        "outcome": "victory",
        "weather": "Perfect sun. Every cloud cleared.",
    },
    {
        "date": "Year 1528",
        "title": "The Marineford War — The Day We Lost",
        "entry": "We couldn't save Ace. The world showed us exactly how small we still are. Luffy cried on an island for days. Then he got back up.",
        "location": "Marineford",
        "outcome": "loss",
        "weather": "Fire everywhere. Sky was red.",
    },
    {
        "date": "Year 1531",
        "title": "Wano Kuni — We Toppled a Yonko",
        "entry": "One dragon emperor. Twenty thousand soldiers. One Straw Hat crew plus allies. Somehow the math worked in our favor. Zoro cut a mountain.",
        "location": "Wano Kuni",
        "outcome": "victory",
        "weather": "Started grim. Ended with fireworks.",
    },
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "crew": CREW,
            "wanted": WANTED,
            "islands": ISLANDS,
            "adventure_log": ADVENTURE_LOG,
        },
    )


@app.get("/api/islands")
async def get_islands():
    return {"islands": ISLANDS}


@app.get("/api/crew")
async def get_crew():
    return {"crew": CREW}
