#!/usr/bin/env python3
"""Genera le pagine dell'anteprima con testata e piede in comune: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
LIVE = "https://www.scrocchia80.no"
NAV = [("butikk.html", "Shop"), ("om-oss.html", "Om oss"), ("bedrift.html", "Er du en bedrift?")]
ADD = "Forhåndsvisning: handlekurven er ikke aktiv ennå."

BASE_SPECS = [
    ("Ingredienser", "Hvetemel type ”0”, vann, solsikkeolje, salt, gjær, malt."),
    ("Allergener", "Kan inneholde spor av soya, sennep, melk, egg, nøtter. Inneholder gluten."),
    ("Holdbarhet", "50 dager i romtemperatur."),
]

PRODUCTS = [
    dict(slug="la-classica", title="Base ‘Classica’", price="kr 65,00", reviews="6 kundeomtaler", images=[0, 1, 2],
         intro=["Laget med italienske mel av høy kvalitet, denne napolitanske-stil basen garanterer en lett og sprø crust, perfekt for de som søker den autentiske smaken av italiensk tradisjon."],
         specs=BASE_SPECS + [("Diameter", "28-30ø"), ("Nettovekt", "250g")]),
    dict(slug="base-romana-2-stk", title="Base ‘Romana’ 2 stk", price="kr 99,00", reviews="1 kundeomtale", images=[0, 1],
         intro=["Inspirert av romersk tradisjon, har denne pizzabasen en tynn og sprø kant. Perfekt for de som elsker en lett pizza med lave kanter og en deilig sprø tekstur."],
         specs=BASE_SPECS + [("Diameter", "28-30ø"), ("Nettovekt", "200g x 2 stk")]),
    dict(slug="pizza-integrale", title="Base ‘Integrale’", price="kr 69,00", reviews="3 kundeomtaler", images=[0, 1, 2],
         intro=["Laget med fullkorn-mel, rik på fiber og ideelt for de som ønsker en sunn kosthold uten å gi avkall på gleden av en autentisk smakende pizza."],
         specs=[("Ingredienser", "Fullkorn durumhvete semulegrynmel, type 2 mykt hvetemel, vann, solsikkeolje, salt, gjær, malt."),
                BASE_SPECS[1], BASE_SPECS[2], ("Diameter", "28-30ø"), ("Nettovekt", "250g")]),
    dict(slug="base-la-pinsa-2-stk", title="Base «La Pinsa» 2 stk", price="kr 109,00", reviews="1 kundeomtale", images=[0],
         intro=["En myk inni og sprø utenfor, laget med en høyt hydrert deig og lang kaldheving som gjør den lett og lettfordøyelig. Den er perfekt for deg som vil nyte en autentisk pinsa hjemme, klar til å toppes med dine favoritingredienser og stekes på få minutter."],
         specs=[("Ingredienser", "Hvetemel type “0”, rismel, soyamel, vann, solsikkeolje, salt, gjær, malt."),
                ("Allergener", "Hvetegluten og soya. Kan inneholde spor av spelt, havre, rug, bygg, sesam, sennep, melk, egg og nøtter. Inneholder gluten."),
                ("Holdbarhet", "50 dager fra produksjonsdato. Se datomerkingen på pakken. Oppbevares tørt og kjølig, i romtemperatur."),
                ("Størrelse", "ca. 15 x 30 cm"), ("Nettovekt", "230 g x 2 stk.")]),
    dict(slug="base-im-not-different", title="Base “I’m not different…”", price="kr 99,90", reviews="3 kundeomtaler", images=[0], tag="Gluten free", tint="#f3f2f0",
         intro=["Not the typical gluten-free base! Ours is inspired by the Neapolitan style: high hydration, airy edges, and a light texture that enhances every topping. Because it’s not different… it’s just gluten free."],
         specs=[("Ingredienser", "Maisstivelse, risstivelse, maismel, maissurdeig, quinoa mel, bok hvete mel, vegetabilske fibre (psyllium, inulin), dekstrose, gjær, solsikkeolje, vann, salt."),
                ("Fortykningsmidler", "guar, E464."),
                ("Kan inneholde spor av", "Soya, Sennep, Melk, Egg, Nøtter, Melkeproteiner og Sesam."),
                ("Holdbarhet", "50 dager i romtemperatur."), ("Diameter", "29ø ca"), ("Nettovekt", "300g ca"),
                ("Næringsinnhold pr 100g", "Energi 363 Kcal, Fett 0,1g (hvorav mettede fettsyrer 0,02g), Karbohydrater 89 g (hvorav sukkerarter 4 g), Protein 0,4 g, Fiber 5,8 g, Salt 0,1 g.")]),
    dict(slug="la-dama", title="La Dama", price="kr 55,00", reviews="", images=[0, 1, 2, 3], tag="Nyheter", subtitle="Mel Tipo «0» La Dama 1 kg",
         intro=["La Dama Tipo 0 er et mel laget av en utvalgt blanding av korn med høyt proteininnhold, noe som gir en stabil og elastisk deig ved middels til lang modning. Dette er et balansert og kraftig mel som samtidig gjør det enkelt å forme og håndtere deigemner, også i profesjonell produksjon.",
                "Skann QR‑koden for å se Scrocchia 80 sin pizza oppskrift!"],
         specs=[], doc=(LIVE + "/wp-content/uploads/2026/05/technical-sheet-La-Dama-1kg.pdf", "Technical sheet La Dama 1kg")),
    dict(slug="la-rossa-by-scrocchia-80", title="La Rossa by Scrocchia 80", price="kr 65,00", reviews="1 kundeomtale", images=[0, 1, 2, 3],
         intro=["A natural, gluten‑free tomato pulp sauce made with chunky tomato pieces, enriched with oregano and basil.",
                "Bright red colour, aromatic profile, and a balanced, slightly rustic texture that enhances both flavour and visual appeal.",
                "Born for pizza, ideal for focaccia, and general food preparation."],
         specs=[("Ingredients", "Tomato pulp, extra virgin olive oil, salt, basil, sugar, oregano. Produced in a facility that uses celery and sulphites."),
                ("Allergens", "The product does not contain: gluten, peanuts, soy, sesame, milk, nuts, eggs, fish, crustaceans, molluscs, lupin, mustard, sulphites >10 mg/kg. Possible presence in production site: celery, sulphites."),
                ("Storing", "Store at room temperature, away from heat and light. Once opened, keep refrigerated and consume within 5 days.")]),
]

BENEFITS = [
    ("Tidsbesparelse", "Slutt å bruke tid på deiger, heving, mel og spesialutstyr! Våre klare-til-bruk pizzabunner lar deg fokusere på det som virkelig betyr noe: å glede kundene dine og skape spesielle øyeblikk."),
    ("Håndverkskvalitet", "Hver bunn er laget for hånd med førsteklasses ingredienser, noe som garanterer at du alltid kan tilby den samme, utmerkede kvaliteten."),
    ("Kostnadsreduksjon", "Du trenger ikke spesialisert personale – hvem som helst kan raskt lære å bruke vårt produkt. Dette gjør at du kan redusere kostnadene uten at det går utover kvaliteten."),
    ("Ingen svinn, ingen problem", "Bruk kun de bunnene du trenger, og reduser både svinn og kostnader. Regenerer kun det som er nødvendig."),
    ("Lett å oppbevare", "Pizzabunnene kan oppbevares i romtemperatur, noe som sparer plass og kostnader. De har en holdbarhet på opptil 50 dager, noe som garanterer både friskhet og praktisk bruk. Perfekt for enhver anledning!"),
    ("Kreativ frihet", "Våre pizzabunner gir deg fleksibiliteten til å realisere dine kulinariske ideer! Perfekte for restauratører og entusiaster, lar de deg lage unike og deilige pizzaer til enhver anledning."),
]

INGREDIENTS = [
    ("Mel", "Vi bruker mel av høy kvalitet, malt på stein, for å gi våre pizzabunner en perfekt konsistens og autentisk smak. Utvalget av mel sikrer optimal heving og sprø skorpe."),
    ("Vann", "Vann er en grunnleggende ingrediens for deigen. Vi velger rent og forurensningsfritt vann, som bidrar til å oppnå myk konsistens og jevn heving."),
    ("Naturlig gjær", "Vi bruker surdeig for å gi våre pizzabunner en unik smak og bedre fordøyelighet. Naturlig gjær fremmer langsom fermentering, som utvikler uforglemmelige aromaer og smaker."),
    ("Havsalt", "Vi tilsetter havsalt for å forsterke smaken av ingrediensene og forbedre deigens struktur. Salt er essensielt for korrekt heving og for å balansere smakene."),
    ("Solsikkeolje", "En nøytral olje som sikrer optimal sprøhet og en jevn gyllen farge ved steking."),
    ("Naturlige ingredienser uten konserveringsmidler", "Vi tilbyr produkter uten konserveringsmidler og kjemiske tilsetningsstoffer. Alle våre ingredienser er naturlige og nøye utvalgte for å sikre en autentisk gastronomisk opplevelse."),
]


def image(product, index=0):
    return f"assets/products/{product['slug']}-{index}.jpg"


def card(product):
    dark = " dark" if product.get("dark") else ""
    tint = f' style="background:{product["tint"]}"' if product.get("tint") else ""
    href = f"produkt-{product['slug']}.html"
    return f"""
  <article class="product-card reveal">
    <a class="thumb{dark}" href="{href}"{tint}><img src="{image(product)}" alt="{product['title']}" loading="lazy"></a>
    <h3><a href="{href}">{product['title']}</a></h3>
    <p class="price">{product['price']}</p>
    <button class="btn" type="button" data-demo="{ADD}">Legg i handlekurv</button>
  </article>"""


def page(filename, title, description, body, current=None):
    nav = "".join(f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for href, label in NAV[:2])
    nav += f'<a class="wide" href="bedrift.html"{" aria-current=\"page\"" if current == "bedrift.html" else ""}>Bedrift</a>'
    html = f"""<!doctype html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="styles.css">
<script src="site.js"></script>
</head>
<body>
<a class="skip" href="#main">Hopp til innhold</a>
<p class="notice">Fri frakt for bestillinger over 699 nok!</p>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="index.html" aria-label="Scrocchia 80, hjem"><img src="assets/logo-full.png" alt="Scrocchia 80"></a>
    <nav class="site-nav" aria-label="Hovedmeny">{nav}
      <button class="cart" type="button" data-demo="{ADD}"><span class="label">Handlekurv</span><b>0</b></button>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <a class="footer-logo" href="index.html" aria-label="Scrocchia 80, hjem"><img src="assets/logo-full.png" alt="Scrocchia 80"></a>
  <div class="footer-cols">
    <div><h2>Kontakt</h2><ul>
      <li>Adresse: Skærdalen 38, 3533 Tyristrand</li>
      <li>E-post: <a href="mailto:post@scrocchia80.no">post@scrocchia80.no</a></li>
      <li>Mobiltelefon: 94 46 18 15</li>
      <li>Org.Nr: 93 42 68 083</li>
    </ul></div>
    <div><h2>Utforsk</h2><ul>
      <li><a href="butikk.html">Shop</a></li>
      <li><a href="om-oss.html">Om oss</a></li>
      <li><a href="bedrift.html">Er du en bedrift?</a></li>
      <li><a href="{LIVE}/termini-e-condizioni/" target="_blank" rel="noopener noreferrer">Vilkår og betingelser</a></li>
    </ul></div>
    <div><h2>Følg oss</h2><ul>
      <li><a href="https://www.facebook.com/profile.php?id=61566819995526" target="_blank" rel="noopener noreferrer">Facebook</a></li>
      <li><a href="https://www.instagram.com/scrocchia_80" target="_blank" rel="noopener noreferrer">Instagram</a></li>
    </ul></div>
  </div>
  <p class="footer-bottom">© Scrocchia 80</p>
</footer>
<div class="toast" role="status"></div>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


benefits = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in BENEFITS)
ingredients = "".join(f'<li><span>{i}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(INGREDIENTS, 1))

page("index.html", "Scrocchia 80 – Håndlagde pizzabunner", "Håndlagde pizzabunner for restauranter og matglade hjemme.", f"""
<section class="hero">
  <div class="reveal">
    <h1>Alle har rett til å spise en <em>god pizza</em></h1>
    <p class="lede">Revolusjoner menyen din og din kulinariske opplevelse med våre håndlagde pizzabunner! Perfekte både for restaurantløsninger og matglade hjemme.</p>
    <div class="actions">
      <a class="btn btn-red" href="butikk.html">Besøk vår e-butikk</a>
      <a class="btn" href="bedrift.html">Er du en bedrift?</a>
    </div>
  </div>
  <div class="hero-photo reveal">
    <img src="assets/integrale2-1536x1152.jpg" alt="En nystekt pizza fra Scrocchia 80 med luftig, sprø kant">
    <span class="hero-badge">Holdbarhet opptil 50 dager</span>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="head-row reveal">
    <div><p class="eyebrow">Shop</p><h2 class="title">Velg din bunn</h2></div>
    <a class="btn" href="butikk.html">Se alle produkter</a>
  </div>
  <div class="products">{''.join(card(p) for p in PRODUCTS[:4])}
  </div>
</section>

<section class="section craft">
  <img class="reveal" src="assets/pizza-la-classica-1403x1536.jpeg" alt="Pizzabunn sett ovenfra" loading="lazy">
  <div class="reveal">
    <p class="eyebrow">Hvorfor velge våre pizzabunner?</p>
    <h2 class="title">Håndverk og smak</h2>
    <p class="lede">Spar tid og lever eksepsjonell kvalitet hver gang! Våre ferdige pizzabunner er den ideelle løsningen for de som ønsker å servere en autentisk og velsmakende pizza uten stresset med å lage deigen selv.</p>
    <strong>Din suksess er vår prioritet!</strong>
    <div class="actions"><a class="btn" href="om-oss.html">Lær mer!</a></div>
  </div>
</section>

<section class="section">
  <div class="head-row reveal"><h2 class="title">Fordelene med våre produkter</h2></div>
  <ul class="benefits">{benefits}</ul>
</section>

<section class="section ingredients">
  <div class="media reveal"><video data-lazy="assets/hero-540.mp4" muted loop playsinline aria-label="Mel som renner gjennom en hånd ned i en bolle"></video></div>
  <div class="reveal">
    <p class="eyebrow">Våre ingredienser</p>
    <h2 class="title">Utvalgte, ferske og ekte</h2>
    <p class="lede">Hos Scrocchia80 er kvaliteten på våre pizzabunner vår høyeste prioritet. Vi er stolte av å bruke utvalgte, ferske og ekte ingredienser for å garantere et sluttprodukt som tilfredsstiller alles smak.</p>
    <ol class="ingredient-list">{ingredients}</ol>
    <p class="closing">Kombinasjonen av disse ingrediensene, bearbeidet med lidenskap og omtanke, gjør at vi kan lage pizzabunner som ikke bare er deilige, men også sunne. Hos Scrocchia80 forteller hver bit historien om tradisjon og kjærlighet til ekte matlaging.</p>
  </div>
</section>
""")

page("butikk.html", "Shop – Scrocchia 80", "Pizzabunner, mel og tomatsaus fra Scrocchia 80.", f"""
<header class="page-head reveal"><h1>Shop</h1><p class="lede">Fri frakt for bestillinger over 699 nok!</p></header>
<section class="shop-grid"><div class="products">{''.join(card(p) for p in PRODUCTS)}
</div></section>
""", "butikk.html")

for p in PRODUCTS:
    dark = ' class="dark"' if p.get("dark") else ""
    tint = f' style="background:{p["tint"]}"' if p.get("tint") else ""
    figures = "".join(f'<figure{dark}{tint}><img src="{image(p, i)}" alt="{p["title"]}"></figure>' for i in p["images"])
    specs = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["specs"])
    intro = "".join(f"<p>{t}</p>" for t in p["intro"])
    tag = f'<p class="eyebrow">{p["tag"]}</p>' if p.get("tag") else ""
    page(f"produkt-{p['slug']}.html", f"{p['title']} – Scrocchia 80", p["intro"][0][:150], f"""
<section class="product">
  <div class="gallery reveal{' three' if len(p['images']) == 4 else ''}">{figures}</div>
  <div class="product-info reveal">
    <a class="back" href="butikk.html">← Tilbake til shop</a>
    {tag}
    <h1>{p['title']}</h1>
    {f'<p class="reviews">{p["subtitle"]}</p>' if p.get("subtitle") else ''}
    <p class="price">{p['price']}</p>
    {f'<p class="reviews">{p["reviews"]}</p>' if p['reviews'] else ''}
    <div class="intro">{intro}</div>
    <div class="actions"><button class="btn btn-red" type="button" data-demo="{ADD}">Legg i handlekurv</button></div>
    {f'<dl class="specs">{specs}</dl>' if specs else ''}
    {f'<a class="doc-link" href="{p["doc"][0]}" target="_blank" rel="noopener noreferrer">{p["doc"][1]}</a>' if p.get("doc") else ''}
  </div>
</section>
""", "butikk.html")

page("om-oss.html", "Om oss – Scrocchia 80", "Et lite, men lidenskapelig selskap grunnlagt i hjertet av Oslo.", """
<header class="page-head reveal"><p class="eyebrow">Om oss</p><h1 style="margin-top:.9rem">Velkommen til Scrocchia 80</h1></header>
<section class="about-grid">
  <div class="block reveal">
    <h2>Lidenskap for ekte pizza</h2>
    <p>Vi er et lite, men lidenskapelig selskap grunnlagt i hjertet av Oslo, Norge. Som italienere er vår misjon enkel: å dele vår kjærlighet for autentisk, håndverksmessig pizza med dere. Hos oss kombinerer vi tradisjonell håndverksbaking med innovative løsninger for å skape pizzabunner som tilbyr den perfekte balansen mellom sprøhet, smak og kvalitet.</p>
    <p>Vi har viet mye tid og omtanke til å utvikle en unik oppskrift for deigen, og hver pizzabunn vi produserer er laget med maksimal innsats for å sikre høye standarder, både i smak og praktisk bruk. Enten det er en travel dag eller en spesiell anledning, gjør vårt produkt det enklere for restauranter og matentusiaster å servere autentisk og deilig pizza.</p>
  </div>
  <div class="block reveal">
    <h2>Det handler om mer enn bare pizza</h2>
    <p>For oss handler det om å samle folk gjennom ekstraordinære kulinariske opplevelser. Vi tror på verdien av kvalitetsingredienser, ekte håndverk, og den spesielle følelsen man får av å dele et måltid med mennesker man setter pris på.</p>
    <p>Når du velger Scrocchia 80, kjøper du ikke bare et produkt – du velger en partner som deler din lidenskap for god mat og som er dedikert til å hjelpe deg med å oppnå suksess. Vi er stolte av å bevare den rike tradisjonen med pizza, samtidig som vi tilfører innovasjon og kvalitet i hver fase av prosessen vår.</p>
    <p>Vi ser frem til å følge deg i din reise mot den perfekte pizzabiten!</p>
  </div>
</section>
<section class="team" aria-label="Teamet">
  <img class="reveal" src="assets/team-p1.jpg" alt="Fra Scrocchia 80-teamet, med en pizzaspade" loading="lazy">
  <img class="reveal" src="assets/team-p3.jpg" alt="Fra Scrocchia 80-teamet, med en kjevle" loading="lazy">
  <img class="reveal" src="assets/team-p5.jpg" alt="Fra Scrocchia 80-teamet, med en pizzabunn i hendene" loading="lazy">
  <img class="reveal" src="assets/team-p2.jpg" alt="Fra Scrocchia 80-teamet" loading="lazy">
  <img class="reveal" src="assets/team-p4.jpg" alt="Fra Scrocchia 80-teamet" loading="lazy">
  <img class="reveal" src="assets/team-p6.jpg" alt="Fra Scrocchia 80-teamet" loading="lazy">
</section>
<section class="section pull"><blockquote class="reveal">«Vi er stolte av de resultatene vi har oppnådd, og vi tror fast at pizzabunnene fra Scrocchia 80 kan konkurrere ikke bare med våre direkte konkurrenter, men også med ulike tradisjonelle pizzerias»</blockquote></section>
""", "om-oss.html")

page("bedrift.html", "Er du en bedrift? – Scrocchia 80", "Skreddersydde løsninger for selskaper og forhandlere.", """
<header class="page-head reveal"><p class="eyebrow">Kontakt oss</p><h1 style="margin-top:.9rem">Er du en bedrift?</h1></header>
<section class="business">
  <div class="copy reveal">
    <p class="lede">Er du et selskap eller en forhandler interessert i å kjøpe våre pizzabunner? Vi er her for å støtte deg! Kontakt oss for å oppdage våre tilbud og hvordan vi kan imøtekomme dine behov.</p>
    <p style="margin-top:1.25rem">Vi tilbyr skreddersydde løsninger for fagfolk i bransjen som ønsker å integrere våre produkter av høy kvalitet i sitt sortiment. For å motta mer informasjon eller be om et pristilbud, inviterer vi deg til å fylle ut skjemaet nedenfor.</p>
    <p>Vårt dedikerte team vil svare deg raskt og gi deg detaljer om priser, salgsbetingelser og fraktmetoder. Ikke nøl med å kontakte oss for å diskutere et gunstig og tilpasset samarbeid!</p>
  </div>
  <form class="form reveal">
    <label class="field"><span>Fornavn *</span><input name="first" required autocomplete="given-name"></label>
    <label class="field"><span>Etternavn *</span><input name="last" required autocomplete="family-name"></label>
    <label class="field"><span>Bedrift navn *</span><input name="company" required autocomplete="organization"></label>
    <label class="field"><span>Org. nr. *</span><input name="org" required></label>
    <label class="field full"><span>E-post *</span><input name="email" type="email" required autocomplete="email"></label>
    <label class="field full"><span>Emne *</span><input name="subject" required></label>
    <label class="field full"><span>Kommentar eller melding</span><textarea name="message" rows="5"></textarea></label>
    <div><button class="btn btn-red" type="submit">Send</button></div>
    <p class="form-note" role="status"></p>
  </form>
</section>
""", "bedrift.html")
