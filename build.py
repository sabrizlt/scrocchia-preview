#!/usr/bin/env python3
"""Genera le pagine nelle tre lingue (norvegese nella radice, en/ e it/): python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
LIVE = "https://www.scrocchia80.no"
LANGS = {"nb": ("", "Norsk", "NO"), "en": ("en/", "English", "EN"), "it": ("it/", "Italiano", "IT")}


def T(nb, en, it):
    return {"nb": nb, "en": en, "it": it}


FLAGS = {
    "nb": '<svg viewBox="0 0 22 16" aria-hidden="true"><rect width="22" height="16" fill="#ba0c2f"/><path d="M6 0h4v16H6zM0 6h22v4H0z" fill="#fff"/><path d="M7 0h2v16H7zM0 7h22v2H0z" fill="#00205b"/></svg>',
    "en": '<svg viewBox="0 0 60 30" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="30" fill="#012169"/><path d="M0 0l60 30M60 0L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30M60 0L0 30" stroke="#c8102e" stroke-width="2.5"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#c8102e" stroke-width="6"/></svg>',
    "it": '<svg viewBox="0 0 3 2" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="3" height="2" fill="#fff"/><rect width="1" height="2" fill="#009246"/><rect x="2" width="1" height="2" fill="#ce2b37"/></svg>',
}

UI = dict(
    menu=T("Meny", "Menu", "Menu"),
    notice=T("Fri frakt for bestillinger over 699 nok!", "Free shipping on orders over 699 NOK!", "Spedizione gratuita per ordini superiori a 699 NOK!"),
    about=T("Om oss", "About us", "Su di noi"),
    business_short=T("Bedrift", "Business", "Aziende"),
    business=T("Er du en bedrift?", "Are you a business?", "Sei un'azienda?"),
    cart=T("Handlekurv", "Basket", "Carrello"),
    add=T("Legg i handlekurv", "Add to basket", "Aggiungi al carrello"),
    demo=T("Forhåndsvisning: handlekurven er ikke aktiv ennå.", "Preview: the basket is not active yet.", "Anteprima: il carrello non è ancora attivo."),
    form_demo=T("Forhåndsvisning: skjemaet sender ingenting ennå.", "Preview: this form does not send anything yet.", "Anteprima: il modulo non invia ancora nulla."),
    skip=T("Hopp til innhold", "Skip to content", "Vai al contenuto"),
    contact=T("Kontakt", "Contact", "Contatti"),
    address=T("Adresse", "Address", "Indirizzo"),
    email=T("E-post", "Email", "Email"),
    phone=T("Mobiltelefon", "Mobile", "Cellulare"),
    org=T("Org.Nr", "Org. No.", "Org. n."),
    explore=T("Utforsk", "Explore", "Esplora"),
    follow=T("Følg oss", "Follow us", "Seguici"),
    terms=T("Vilkår og betingelser", "Terms and conditions", "Termini e condizioni"),
    back=T("← Tilbake til shop", "← Back to shop", "← Torna allo shop"),
    all_products=T("Se alle produkter", "See all products", "Vedi tutti i prodotti"),
    choose=T("Velg din bunn", "Choose your base", "Scegli la tua base"),
    reviews1=T("kundeomtale", "customer review", "recensione"),
    reviewsN=T("kundeomtaler", "customer reviews", "recensioni"),
    subtitle=T("Håndlagde pizzabunner", "Handmade pizza bases", "Basi pizza artigianali"),
)

# Campi fissi delle schede
K = dict(
    ing=T("Ingredienser", "Ingredients", "Ingredienti"),
    all=T("Allergener", "Allergens", "Allergeni"),
    life=T("Holdbarhet", "Shelf life", "Conservazione"),
    dia=T("Diameter", "Diameter", "Diametro"),
    wt=T("Nettovekt", "Net weight", "Peso netto"),
    size=T("Størrelse", "Size", "Dimensioni"),
    thick=T("Fortykningsmidler", "Thickeners", "Addensanti"),
    trace=T("Kan inneholde spor av", "May contain traces of", "Può contenere tracce di"),
    nutri=T("Næringsinnhold pr 100g", "Nutrition per 100g", "Valori nutrizionali per 100g"),
    store=T("Oppbevaring", "Storage", "Conservazione"),
)
ALLERGENS = T("Kan inneholde spor av soya, sennep, melk, egg, nøtter. Inneholder gluten.",
              "May contain traces of soy, mustard, milk, eggs, nuts. Contains gluten.",
              "Può contenere tracce di soia, senape, latte, uova, frutta a guscio. Contiene glutine.")
LIFE = T("50 dager i romtemperatur.", "50 days at room temperature.", "50 giorni a temperatura ambiente.")
WHEAT = T("Hvetemel type ”0”, vann, solsikkeolje, salt, gjær, malt.", "Type “0” wheat flour, water, sunflower oil, salt, yeast, malt.", "Farina di grano tipo “0”, acqua, olio di semi di girasole, sale, lievito, malto.")
DIA = T("28-30ø", "28-30 cm", "28-30 cm")

PRODUCTS = [
    dict(slug="la-classica", title="Base ‘Classica’", price="kr 65,00", reviews=6, images=[0, 1, 2],
         intro=[T("Laget med italienske mel av høy kvalitet, denne napolitanske-stil basen garanterer en lett og sprø crust, perfekt for de som søker den autentiske smaken av italiensk tradisjon.",
                  "Made with high-quality Italian flour, this Neapolitan-style base guarantees a light, crispy crust, perfect for those looking for the authentic taste of Italian tradition.",
                  "Realizzata con farine italiane di alta qualità, questa base in stile napoletano garantisce una crosta leggera e croccante, perfetta per chi cerca il sapore autentico della tradizione italiana.")],
         specs=[("ing", WHEAT), ("all", ALLERGENS), ("life", LIFE), ("dia", DIA), ("wt", T("250g", "250 g", "250 g"))]),
    dict(slug="base-romana-2-stk", title="Base ‘Romana’ 2 stk", price="kr 99,00", reviews=1, images=[0, 1],
         intro=[T("Inspirert av romersk tradisjon, har denne pizzabasen en tynn og sprø kant. Perfekt for de som elsker en lett pizza med lave kanter og en deilig sprø tekstur.",
                  "Inspired by Roman tradition, this pizza base has a thin, crispy edge. Perfect for those who love a light pizza with low edges and a deliciously crisp texture.",
                  "Ispirata alla tradizione romana, questa base pizza ha un bordo sottile e croccante. Perfetta per chi ama una pizza leggera, con bordi bassi e una deliziosa consistenza croccante.")],
         specs=[("ing", WHEAT), ("all", ALLERGENS), ("life", LIFE), ("dia", DIA), ("wt", T("200g x 2 stk", "200 g x 2 pcs", "200 g x 2 pz"))]),
    dict(slug="pizza-integrale", title="Base ‘Integrale’", price="kr 69,00", reviews=3, images=[0, 1, 2],
         intro=[T("Laget med fullkorn-mel, rik på fiber og ideelt for de som ønsker en sunn kosthold uten å gi avkall på gleden av en autentisk smakende pizza.",
                  "Made with wholegrain flour, rich in fibre and ideal for those who want a healthy diet without giving up the pleasure of an authentic-tasting pizza.",
                  "Realizzata con farina integrale, ricca di fibre e ideale per chi desidera un'alimentazione sana senza rinunciare al piacere di una pizza dal sapore autentico.")],
         specs=[("ing", T("Fullkorn durumhvete semulegrynmel, type 2 mykt hvetemel, vann, solsikkeolje, salt, gjær, malt.",
                          "Wholegrain durum wheat semolina, type 2 soft wheat flour, water, sunflower oil, salt, yeast, malt.",
                          "Semola integrale di grano duro, farina di grano tenero tipo 2, acqua, olio di semi di girasole, sale, lievito, malto.")),
                ("all", ALLERGENS), ("life", LIFE), ("dia", DIA), ("wt", T("250g", "250 g", "250 g"))]),
    dict(slug="base-la-pinsa-2-stk", title="Base «La Pinsa» 2 stk", price="kr 109,00", reviews=1, images=[0],
         intro=[T("En myk inni og sprø utenfor, laget med en høyt hydrert deig og lang kaldheving som gjør den lett og lettfordøyelig. Den er perfekt for deg som vil nyte en autentisk pinsa hjemme, klar til å toppes med dine favoritingredienser og stekes på få minutter.",
                  "Soft inside and crispy outside, made with a highly hydrated dough and a long cold rise that makes it light and easy to digest. Perfect if you want to enjoy an authentic pinsa at home, ready to be topped with your favourite ingredients and baked in minutes.",
                  "Morbida dentro e croccante fuori, realizzata con un impasto ad alta idratazione e una lunga lievitazione a freddo che la rendono leggera e digeribile. Perfetta per gustare una vera pinsa a casa, pronta da condire con i tuoi ingredienti preferiti e da cuocere in pochi minuti.")],
         specs=[("ing", T("Hvetemel type “0”, rismel, soyamel, vann, solsikkeolje, salt, gjær, malt.",
                          "Type “0” wheat flour, rice flour, soy flour, water, sunflower oil, salt, yeast, malt.",
                          "Farina di grano tipo “0”, farina di riso, farina di soia, acqua, olio di semi di girasole, sale, lievito, malto.")),
                ("all", T("Hvetegluten og soya. Kan inneholde spor av spelt, havre, rug, bygg, sesam, sennep, melk, egg og nøtter. Inneholder gluten.",
                          "Wheat gluten and soy. May contain traces of spelt, oats, rye, barley, sesame, mustard, milk, eggs and nuts. Contains gluten.",
                          "Glutine di frumento e soia. Può contenere tracce di farro, avena, segale, orzo, sesamo, senape, latte, uova e frutta a guscio. Contiene glutine.")),
                ("life", T("50 dager fra produksjonsdato. Se datomerkingen på pakken. Oppbevares tørt og kjølig, i romtemperatur.",
                           "50 days from the production date. See the date on the pack. Store in a cool, dry place, at room temperature.",
                           "50 giorni dalla data di produzione. Vedi la data sulla confezione. Conservare in luogo fresco e asciutto, a temperatura ambiente.")),
                ("size", T("ca. 15 x 30 cm", "approx. 15 x 30 cm", "circa 15 x 30 cm")), ("wt", T("230 g x 2 stk.", "230 g x 2 pcs", "230 g x 2 pz"))]),
    dict(slug="base-im-not-different", title="Base “I’m not different…”", price="kr 99,90", reviews=3, images=[0], tag="Gluten free", tint="#f3f2f0",
         intro=[T("Not the typical gluten-free base! Ours is inspired by the Neapolitan style: high hydration, airy edges, and a light texture that enhances every topping. Because it’s not different… it’s just gluten free.",
                  "Not the typical gluten-free base! Ours is inspired by the Neapolitan style: high hydration, airy edges, and a light texture that enhances every topping. Because it’s not different… it’s just gluten free.",
                  "Non la solita base senza glutine! La nostra si ispira allo stile napoletano: alta idratazione, bordi ariosi e una consistenza leggera che esalta ogni condimento. Perché non è diversa… è solo senza glutine.")],
         specs=[("ing", T("Maisstivelse, risstivelse, maismel, maissurdeig, quinoa mel, bok hvete mel, vegetabilske fibre (psyllium, inulin), dekstrose, gjær, solsikkeolje, vann, salt.",
                          "Corn starch, rice starch, corn flour, corn sourdough, quinoa flour, buckwheat flour, vegetable fibres (psyllium, inulin), dextrose, yeast, sunflower oil, water, salt.",
                          "Amido di mais, amido di riso, farina di mais, lievito madre di mais, farina di quinoa, farina di grano saraceno, fibre vegetali (psillio, inulina), destrosio, lievito, olio di semi di girasole, acqua, sale.")),
                ("thick", T("guar, E464.", "guar, E464.", "guar, E464.")),
                ("trace", T("Soya, Sennep, Melk, Egg, Nøtter, Melkeproteiner og Sesam.", "Soy, mustard, milk, eggs, nuts, milk proteins and sesame.", "Soia, senape, latte, uova, frutta a guscio, proteine del latte e sesamo.")),
                ("life", LIFE), ("dia", T("29ø ca", "approx. 29 cm", "circa 29 cm")), ("wt", T("300g ca", "approx. 300 g", "circa 300 g")),
                ("nutri", T("Energi 363 Kcal, Fett 0,1g (hvorav mettede fettsyrer 0,02g), Karbohydrater 89 g (hvorav sukkerarter 4 g), Protein 0,4 g, Fiber 5,8 g, Salt 0,1 g.",
                            "Energy 363 kcal, fat 0.1 g (of which saturates 0.02 g), carbohydrates 89 g (of which sugars 4 g), protein 0.4 g, fibre 5.8 g, salt 0.1 g.",
                            "Energia 363 kcal, grassi 0,1 g (di cui saturi 0,02 g), carboidrati 89 g (di cui zuccheri 4 g), proteine 0,4 g, fibre 5,8 g, sale 0,1 g."))]),
    dict(slug="la-dama", title="La Dama", price="kr 55,00", reviews=0, images=[0, 1, 2, 3], tag=T("Nyheter", "New", "Novità"),
         subtitle=T("Mel Tipo «0» La Dama 1 kg", "La Dama Type “0” flour, 1 kg", "Farina Tipo «0» La Dama 1 kg"),
         intro=[T("La Dama Tipo 0 er et mel laget av en utvalgt blanding av korn med høyt proteininnhold, noe som gir en stabil og elastisk deig ved middels til lang modning. Dette er et balansert og kraftig mel som samtidig gjør det enkelt å forme og håndtere deigemner, også i profesjonell produksjon.",
                  "La Dama Tipo 0 is a flour made from a selected blend of high-protein grains, giving a stable, elastic dough with medium to long maturation. It is a balanced, strong flour that also makes dough balls easy to shape and handle, including in professional production.",
                  "La Dama Tipo 0 è una farina ottenuta da una miscela selezionata di grani ad alto contenuto proteico, che dà un impasto stabile ed elastico con maturazioni medio-lunghe. È una farina equilibrata e forte, che rende facile formare e lavorare i panetti, anche nella produzione professionale."),
                T("Skann QR‑koden for å se Scrocchia 80 sin pizza oppskrift!", "Scan the QR code to see Scrocchia 80's pizza recipe!", "Scansiona il codice QR per vedere la ricetta della pizza di Scrocchia 80!")],
         specs=[], doc=(LIVE + "/wp-content/uploads/2026/05/technical-sheet-La-Dama-1kg.pdf", "Technical sheet La Dama 1kg")),
    dict(slug="la-rossa-by-scrocchia-80", title="La Rossa by Scrocchia 80", price="kr 65,00", reviews=1, images=[0, 1, 2, 3],
         intro=[T("A natural, gluten‑free tomato pulp sauce made with chunky tomato pieces, enriched with oregano and basil.",
                  "A natural, gluten‑free tomato pulp sauce made with chunky tomato pieces, enriched with oregano and basil.",
                  "Una salsa naturale di polpa di pomodoro senza glutine, con pezzi di pomodoro, arricchita con origano e basilico."),
                T("Bright red colour, aromatic profile, and a balanced, slightly rustic texture that enhances both flavour and visual appeal.",
                  "Bright red colour, aromatic profile, and a balanced, slightly rustic texture that enhances both flavour and visual appeal.",
                  "Colore rosso brillante, profilo aromatico e una consistenza equilibrata, leggermente rustica, che esalta sapore e aspetto."),
                T("Born for pizza, ideal for focaccia, and general food preparation.",
                  "Born for pizza, ideal for focaccia, and general food preparation.",
                  "Nata per la pizza, ideale per la focaccia e per le preparazioni in cucina.")],
         specs=[("ing", T("Tomato pulp, extra virgin olive oil, salt, basil, sugar, oregano. Produced in a facility that uses celery and sulphites.",
                          "Tomato pulp, extra virgin olive oil, salt, basil, sugar, oregano. Produced in a facility that uses celery and sulphites.",
                          "Polpa di pomodoro, olio extravergine di oliva, sale, basilico, zucchero, origano. Prodotta in uno stabilimento che utilizza sedano e solfiti.")),
                ("all", T("The product does not contain: gluten, peanuts, soy, sesame, milk, nuts, eggs, fish, crustaceans, molluscs, lupin, mustard, sulphites >10 mg/kg. Possible presence in production site: celery, sulphites.",
                          "The product does not contain: gluten, peanuts, soy, sesame, milk, nuts, eggs, fish, crustaceans, molluscs, lupin, mustard, sulphites >10 mg/kg. Possible presence in production site: celery, sulphites.",
                          "Il prodotto non contiene: glutine, arachidi, soia, sesamo, latte, frutta a guscio, uova, pesce, crostacei, molluschi, lupini, senape, solfiti >10 mg/kg. Possibile presenza nello stabilimento: sedano, solfiti.")),
                ("store", T("Store at room temperature, away from heat and light. Once opened, keep refrigerated and consume within 5 days.",
                            "Store at room temperature, away from heat and light. Once opened, keep refrigerated and consume within 5 days.",
                            "Conservare a temperatura ambiente, lontano da fonti di calore e luce. Dopo l'apertura, conservare in frigorifero e consumare entro 5 giorni."))]),
]

BENEFITS = [
    T(("Tidsbesparelse", "Slutt å bruke tid på deiger, heving, mel og spesialutstyr! Våre klare-til-bruk pizzabunner lar deg fokusere på det som virkelig betyr noe: å glede kundene dine og skape spesielle øyeblikk."),
      ("Save time", "We do the prep for you. Our ready-to-use bases let you focus on what matters most: delighting your customers."),
      ("Risparmio di tempo", "Basta perdere tempo con impasti, lievitazioni, farine e attrezzature! Le nostre basi pronte all’uso ti permettono di concentrarti su ciò che conta di più: deliziare i tuoi clienti e creare momenti speciali.")),
    T(("Håndverkskvalitet", "Hver bunn er laget for hånd med førsteklasses ingredienser, noe som garanterer at du alltid kan tilby den samme, utmerkede kvaliteten."),
      ("Artisanal quality", "Each base is made with premium ingredients, ensuring you deliver the same excellent quality every time."),
      ("Qualità artigianale", "Ogni base è realizzata a mano con ingredienti di prima scelta, garantendoti di offrire la stessa eccellente qualità ogni volta.")),
    T(("Kostnadsreduksjon", "Du trenger ikke spesialisert personale – hvem som helst kan raskt lære å bruke vårt produkt. Dette gjør at du kan redusere kostnadene uten at det går utover kvaliteten."),
      ("Cost reduction", "No need for specialist staff – anyone can be quickly trained to prepare our product with ease."),
      ("Riduzione dei costi", "Non serve personale specializzato: chiunque può imparare rapidamente a usare il nostro prodotto. Questo ti consente di abbattere i costi senza compromettere la qualità.")),
    T(("Ingen svinn, ingen problem", "Bruk kun de bunnene du trenger, og reduser både svinn og kostnader. Regenerer kun det som er nødvendig."),
      ("No waste, no hassle", "Use only the bases you need, reducing both waste and costs. Regenerate only what you need."),
      ("Nessuno spreco, nessun problema", "Utilizza solo le basi di cui hai bisogno, riducendo sia gli sprechi che i costi. Rigenera solo ciò che serve.")),
    T(("Lett å oppbevare", "Pizzabunnene kan oppbevares i romtemperatur, noe som sparer plass og kostnader. De har en holdbarhet på opptil 50 dager, noe som garanterer både friskhet og praktisk bruk. Perfekt for enhver anledning!"),
      ("Easy to store", "Our pizza bases can be stored at room temperature, eliminating the need for fridges or freezers, saving space and money."),
      ("Facile da conservare", "Le basi pizza si conservano a temperatura ambiente, risparmiando spazio e costi. Hanno una durata fino a 50 giorni, garantendo freschezza e praticità. Perfette per ogni occasione!")),
    T(("Kreativ frihet", "Våre pizzabunner gir deg fleksibiliteten til å realisere dine kulinariske ideer! Perfekte for restauratører og entusiaster, lar de deg lage unike og deilige pizzaer til enhver anledning."),
      ("Creative freedom", "Our bases adapt to your creativity, allowing you to create pizzas that satisfy every customer request."),
      ("Libertà creativa", "Le nostre basi pizza ti offrono la flessibilità di realizzare le tue idee culinarie! Ideali per ristoratori e appassionati, ti consentono di creare pizze uniche e deliziose per ogni occasione.")),
]

INGREDIENTS = [
    T(("Mel", "Vi bruker mel av høy kvalitet, malt på stein, for å gi våre pizzabunner en perfekt konsistens og autentisk smak. Utvalget av mel sikrer optimal heving og sprø skorpe."),
      ("Flours", "We use a high-quality, stone-ground flour to give our pizza base a perfect consistency and authentic flavor. The selection of soft wheat guarantees optimal leavening and a crispy crust."),
      ("Farine", "Utilizziamo farine di alta qualità, macinate a pietra, per conferire alla nostra base pizza una consistenza perfetta e un sapore autentico. La selezione delle farine garantisce una lievitazione ottimale e una crosta croccante.")),
    T(("Vann", "Vann er en grunnleggende ingrediens for deigen. Vi velger rent og forurensningsfritt vann, som bidrar til å oppnå myk konsistens og jevn heving."),
      ("Water", "Water is a fundamental ingredient for the dough. We choose pure, contaminant-free water, which helps to obtain a soft consistency and uniform leavening."),
      ("Acqua", "L’acqua è un ingrediente fondamentale per l’impasto. Scegliamo acqua pura e priva di contaminanti, che contribuisce a ottenere una consistenza morbida e una lievitazione uniforme.")),
    T(("Naturlig gjær", "Vi bruker surdeig for å gi våre pizzabunner en unik smak og bedre fordøyelighet. Naturlig gjær fremmer langsom fermentering, som utvikler uforglemmelige aromaer og smaker."),
      ("Natural yeast", "We use sourdough to give our pizza bases a unique flavor and superior digestibility. The natural yeast promotes slow fermentation, developing unmistakable aromas and scents."),
      ("Lievito naturale", "Utilizziamo lievito madre per conferire alle nostre basi pizza un sapore unico e una digeribilità superiore. Il lievito naturale favorisce la fermentazione lenta, sviluppando aromi e profumi inconfondibili.")),
    T(("Havsalt", "Vi tilsetter havsalt for å forsterke smaken av ingrediensene og forbedre deigens struktur. Salt er essensielt for korrekt heving og for å balansere smakene."),
      ("Sea salt", "We add sea salt to enhance the flavor of the ingredients and improve the structure of the dough. Salt is essential for proper leavening and to balance the flavors."),
      ("Sale marino", "Aggiungiamo sale marino per esaltare il sapore degli ingredienti e migliorare la struttura dell’impasto. Il sale è essenziale per una corretta lievitazione e per bilanciare i sapori.")),
    T(("Solsikkeolje", "En nøytral olje som sikrer optimal sprøhet og en jevn gyllen farge ved steking."),
      ("Sunflower oil", "A neutral and stable oil that ensures optimal crispness and a uniform golden colour during baking."),
      ("Olio di semi di girasole", "Un olio neutro che assicura una croccantezza ottimale e una doratura uniforme durante la cottura.")),
    T(("Naturlige ingredienser uten konserveringsmidler", "Vi tilbyr produkter uten konserveringsmidler og kjemiske tilsetningsstoffer. Alle våre ingredienser er naturlige og nøye utvalgte for å sikre en autentisk gastronomisk opplevelse."),
      ("Natural ingredients and no preservatives", "We are committed to offering products free from preservatives and chemical additives. All our ingredients are natural and selected to guarantee an authentic gastronomic experience."),
      ("Ingredienti naturali e senza conservanti", "Siamo impegnati a offrire prodotti privi di conservanti e additivi chimici. Tutti i nostri ingredienti sono naturali e selezionati per garantire un’esperienza gastronomica autentica.")),
]

HOME = dict(
    title=T("Scrocchia 80 – Håndlagde pizzabunner", "Scrocchia 80 – Handmade pizza bases", "Scrocchia 80 – Basi pizza artigianali"),
    h1=T("Alle har rett til å spise en <em>god pizza</em>", "Everyone has the right to eat a <em>good pizza</em>", "Tutti hanno il diritto di mangiare un’<em>ottima pizza</em>"),
    lede=T("Revolusjoner menyen din og din kulinariske opplevelse med våre håndlagde pizzabunner! Perfekte både for restaurantløsninger og matglade hjemme.",
           "Revolutionize your menu and your cooking experience with our handmade pizza bases! Perfect for both restaurateurs and home cooks.",
           "Rivoluziona il tuo menu e la tua esperienza culinaria con le nostre basi pizza artigianali! Perfette sia per i ristoratori che per gli amanti della cucina casalinga."),
    shop=T("Besøk vår e-butikk", "Visit the shop", "Visita il negozio"),
    badge=T("Holdbarhet opptil 50 dager", "Shelf life up to 50 days", "Durata fino a 50 giorni"),
    why=T("Hvorfor velge våre pizzabunner?", "Why choose our pizza bases?", "Perché scegliere le nostre basi pizza?"),
    craft=T("Håndverk og smak", "Handcrafted and tasty", "Artigianalità e sapore"),
    craft_text=T("Spar tid og lever eksepsjonell kvalitet hver gang! Våre ferdige pizzabunner er den ideelle løsningen for de som ønsker å servere en autentisk og velsmakende pizza uten stresset med å lage deigen selv.",
                 "Save time and deliver exceptional quality every time! Our ready-to-use pizza bases are the ideal solution for those who want to serve authentic and tasty pizza without the stress of preparing the dough.",
                 "Risparmia tempo e offri una qualità eccezionale ogni volta! Le nostre basi pizza pronte all’uso sono la soluzione ideale per chi desidera servire una pizza autentica e gustosa senza lo stress di preparare l’impasto."),
    success=T("Din suksess er vår prioritet!", "Your success is our priority!", "Il tuo successo è la nostra priorità!"),
    more=T("Lær mer!", "Find out more", "Scopri di più"),
    benefits=T("Fordelene med våre produkter", "The benefits of our products", "I benefici dei nostri prodotti"),
    ing_eye=T("Våre ingredienser", "Our ingredients", "I nostri ingredienti"),
    ing_title=T("Utvalgte, ferske og ekte", "Selected, fresh and genuine", "Selezionati, freschi e genuini"),
    ing_text=T("Hos Scrocchia80 er kvaliteten på våre pizzabunner vår høyeste prioritet. Vi er stolte av å bruke utvalgte, ferske og ekte ingredienser for å garantere et sluttprodukt som tilfredsstiller alles smak.",
               "At Scrocchia 80, the quality of our pizza bases is our priority. We pride ourselves on using only selected, fresh and genuine ingredients to ensure a final product that satisfies everyone’s palate.",
               "Da Scrocchia 80, la qualità delle nostre basi pizza è la nostra priorità. Siamo orgogliosi di utilizzare solo ingredienti selezionati, freschi e genuini, per garantire un prodotto finale che soddisfi il palato di tutti."),
    closing=T("Kombinasjonen av disse ingrediensene, bearbeidet med lidenskap og omtanke, gjør at vi kan lage pizzabunner som ikke bare er deilige, men også sunne. Hos Scrocchia80 forteller hver bit historien om tradisjon og kjærlighet til ekte matlaging.",
              "The combination of these ingredients, worked with passion and attention, allows us to create pizza bases that are not only delicious, but also healthy. At Scrocchia 80, every bite tells the story of tradition and love for genuine cuisine.",
              "La combinazione di questi ingredienti, lavorati con passione e attenzione, ci permette di creare basi pizza che non solo sono deliziose, ma anche sane. Da Scrocchia 80, ogni morso racconta la storia della tradizione e dell’amore per la cucina genuina."),
)

ABOUT = dict(
    welcome=T("Velkommen til Scrocchia 80", "Welcome to Scrocchia 80", "Benvenuti da Scrocchia 80"),
    h2a=T("Lidenskap for ekte pizza", "A passion for real pizza", "La passione per la vera pizza"),
    h2b=T("Det handler om mer enn bare pizza", "It’s more than just pizza", "È di più che una semplice pizza"),
    a=T(["Vi er et lite, men lidenskapelig selskap grunnlagt i hjertet av Oslo, Norge. Som italienere er vår misjon enkel: å dele vår kjærlighet for autentisk, håndverksmessig pizza med dere. Hos oss kombinerer vi tradisjonell håndverksbaking med innovative løsninger for å skape pizzabunner som tilbyr den perfekte balansen mellom sprøhet, smak og kvalitet.",
         "Vi har viet mye tid og omtanke til å utvikle en unik oppskrift for deigen, og hver pizzabunn vi produserer er laget med maksimal innsats for å sikre høye standarder, både i smak og praktisk bruk. Enten det er en travel dag eller en spesiell anledning, gjør vårt produkt det enklere for restauranter og matentusiaster å servere autentisk og deilig pizza."],
        ["A small but passionate company founded in the heart of Oslo, Norway. As Italians, our mission is simple: to share with you our love for authentic artisanal pizza. We combine the tradition of artisanal bread making with innovative solutions to create pizza bases that provide the perfect balance of crunchiness, flavor and quality.",
         "We have spent a lot of time and care in developing a unique recipe for the dough, and every pizza base we produce is made with the utmost effort to ensure high standards in both taste and convenience. Whether it’s a busy day or a special occasion, our product makes it easier for restaurants and food enthusiasts to serve authentic, delicious pizza."],
        ["Una piccola ma appassionata azienda fondata nel cuore di Oslo, in Norvegia. Da italiani la nostra missione è semplice: condividere con voi il nostro amore per la pizza artigianale autentica. Da noi, uniamo la tradizione della panificazione artigianale con soluzioni innovative per creare basi pizza che offrono il perfetto equilibrio tra croccantezza, sapore e qualità.",
         "Abbiamo dedicato molto tempo e cura nello sviluppare una ricetta unica per l’impasto, ogni base pizza che produciamo è realizzata con il massimo impegno per garantire standard elevati sia in termini di gusto che di praticità. Che si tratti di una giornata frenetica o di un’occasione speciale, il nostro prodotto rende più semplice per ristoranti e appassionati di cucina servire una pizza autentica e deliziosa."]),
    b=T(["For oss handler det om å samle folk gjennom ekstraordinære kulinariske opplevelser. Vi tror på verdien av kvalitetsingredienser, ekte håndverk, og den spesielle følelsen man får av å dele et måltid med mennesker man setter pris på.",
         "Når du velger Scrocchia 80, kjøper du ikke bare et produkt – du velger en partner som deler din lidenskap for god mat og som er dedikert til å hjelpe deg med å oppnå suksess. Vi er stolte av å bevare den rike tradisjonen med pizza, samtidig som vi tilfører innovasjon og kvalitet i hver fase av prosessen vår.",
         "Vi ser frem til å følge deg i din reise mot den perfekte pizzabiten!"],
        ["It’s about bringing people together through extraordinary food experiences. We believe in the value of quality ingredients, true craftsmanship, and the special feeling that comes from sharing a meal with the people you love.",
         "When you choose Scrocchia 80, you’re not just buying a product – you’re choosing a partner who shares your passion for good food and is dedicated to helping you achieve success. We’re proud to keep pizza’s rich tradition alive while adding innovation and quality at every step of our process.",
         "We can’t wait to join you on your journey to the perfect bite of pizza!"],
        ["Si tratta di unire le persone attraverso esperienze culinarie straordinarie. Crediamo nel valore degli ingredienti di qualità, del vero artigianato e della sensazione speciale che si prova nel condividere un pasto con le persone a cui si vuole bene.",
         "Quando scegli Scrocchia 80, non acquisti solo un prodotto, scegli un partner che condivide la tua passione per il buon cibo e che è dedicato ad aiutarti a raggiungere il successo. Siamo orgogliosi di mantenere viva la ricca tradizione della pizza italiana, aggiungendo innovazione e qualità in ogni fase del nostro processo.",
         "Non vediamo l’ora di accompagnarti nel tuo viaggio verso il boccone di pizza perfetto!"]),
    quote=T("«Vi er stolte av de resultatene vi har oppnådd, og vi tror fast at pizzabunnene fra Scrocchia 80 kan konkurrere ikke bare med våre direkte konkurrenter, men også med ulike tradisjonelle pizzerias»",
            "“We are proud of the results achieved and firmly believe that Scrocchia 80 pizza bases can compete not only with our direct competitors, but also with several traditional pizzerias”",
            "“Siamo orgogliosi dei risultati ottenuti e crediamo fermamente che le basi pizza di Scrocchia 80 possano competere non solo con i nostri concorrenti diretti, ma anche con diverse pizzerie tradizionali”"),
)

BIZ = dict(
    eye=T("Kontakt oss", "Contact us", "Contattaci"),
    lede=T("Er du et selskap eller en forhandler interessert i å kjøpe våre pizzabunner? Vi er her for å støtte deg! Kontakt oss for å oppdage våre tilbud og hvordan vi kan imøtekomme dine behov.",
           "If you are a company or a retailer interested in purchasing our pizza bases, we are here to support you! Contact us to find out about our offers and how we can meet your needs!",
           "Sei un’azienda o un rivenditore interessato all’acquisto delle nostre basi pizza? Siamo qui per supportarti! Contattaci per scoprire le nostre offerte e come possiamo soddisfare le tue esigenze."),
    p1=T("Vi tilbyr skreddersydde løsninger for fagfolk i bransjen som ønsker å integrere våre produkter av høy kvalitet i sitt sortiment. For å motta mer informasjon eller be om et pristilbud, inviterer vi deg til å fylle ut skjemaet.",
         "We offer customized solutions for industry professionals who want to integrate our high-quality products into their offerings. To receive more information or request a quote, please fill out the form.",
         "Offriamo soluzioni su misura per i professionisti del settore che desiderano integrare i nostri prodotti di alta qualità nella loro gamma. Per ricevere maggiori informazioni o richiedere un preventivo vi invitiamo a compilare il modulo."),
    p2=T("Vårt dedikerte team vil svare deg raskt og gi deg detaljer om priser, salgsbetingelser og fraktmetoder. Ikke nøl med å kontakte oss for å diskutere et gunstig og tilpasset samarbeid!",
         "Our dedicated team will respond promptly, providing you with details on prices, sales conditions and shipping methods. Do not hesitate to contact us to discuss a profitable and personalized collaboration!",
         "Il nostro team dedicato ti risponderà rapidamente e ti fornirà dettagli su prezzi, condizioni di vendita e modalità di spedizione. Non esitate a contattarci per discutere una collaborazione vantaggiosa e personalizzata!"),
    first=T("Fornavn *", "First name *", "Nome *"), last=T("Etternavn *", "Last name *", "Cognome *"),
    company=T("Bedrift navn *", "Company *", "Azienda *"), orgnr=T("Org. nr. *", "Organization number *", "P. IVA *"),
    subject=T("Emne *", "Subject *", "Oggetto *"), msg=T("Kommentar eller melding", "Message", "Commento o messaggio"),
    send=T("Send", "Send", "Invia"),
)


def page(lang, filename, title, description, body, current=None):
    u = lambda key: UI[key][lang]
    up = "../" if LANGS[lang][0] else ""
    switch = "".join(
        f'<a href="{up}{LANGS[other][0]}{filename}" hreflang="{other}" lang="{other}" aria-label="{name}">{FLAGS[other]}</a>'
        for other, (_, name, short) in LANGS.items() if other != lang)
    cur = lambda href: ' aria-current="page"' if href == current else ""
    alternates = "".join(f'<link rel="alternate" hreflang="{o}" href="{up}{LANGS[o][0]}{filename}">' for o in LANGS)
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#2e5a3c">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://sabrizlt.github.io/scrocchia-preview/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://sabrizlt.github.io/scrocchia-preview/{LANGS[lang][0]}{filename}">
{alternates}
<link rel="stylesheet" href="{up}styles.css?v=6">
<script src="{up}site.js?v=6"></script>
</head>
<body data-form-demo="{u('form_demo')}">
<a class="skip" href="#main">{u('skip')}</a>
<p class="notice">{u('notice')}</p>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="index.html" aria-label="Scrocchia 80"><img src="{up}assets/logo-full.png" alt="Scrocchia 80" width="186" height="100"></a>
    <div class="tools">
      <nav class="flags" aria-label="Language">{switch}</nav>
      <button class="cart" type="button" data-demo="{u('demo')}" aria-label="{u('cart')}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l1 13H5L6 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><b>0</b></button>
      <button class="burger" type="button" aria-label="{u('menu')}" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="menu" id="menu" aria-label="{u('menu')}" inert>
  <a href="index.html"{cur('index.html')}>Home</a>
  <a href="butikk.html"{cur('butikk.html')}>Shop</a>
  <a href="om-oss.html"{cur('om-oss.html')}>{u('about')}</a>
  <a href="bedrift.html"{cur('bedrift.html')}>{u('business')}</a>
</nav>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <a class="footer-logo" href="index.html" aria-label="Scrocchia 80"><img src="{up}assets/logo-full.png" alt="Scrocchia 80"></a>
  <div class="footer-cols">
    <div><h2>{u('contact')}</h2><ul>
      <li>{u('address')}: Skærdalen 38, 3533 Tyristrand</li>
      <li>{u('email')}: <a href="mailto:post@scrocchia80.no">post@scrocchia80.no</a></li>
      <li>{u('phone')}: 94 46 18 15</li>
      <li>{u('org')}: 93 42 68 083</li>
    </ul></div>
    <div><h2>{u('explore')}</h2><ul>
      <li><a href="butikk.html">Shop</a></li>
      <li><a href="om-oss.html">{u('about')}</a></li>
      <li><a href="bedrift.html">{u('business')}</a></li>
      <li><a href="{LIVE}/termini-e-condizioni/" target="_blank" rel="noopener noreferrer">{u('terms')}</a></li>
    </ul></div>
    <div><h2>{u('follow')}</h2><ul>
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
    target = ROOT / LANGS[lang][0] / filename
    target.parent.mkdir(exist_ok=True)
    target.write_text(html, encoding="utf-8")


def build(lang):
    up = "../" if LANGS[lang][0] else ""
    u = lambda key: UI[key][lang]
    img = lambda p, i=0: f"{up}assets/products/{p['slug']}-{i}.jpg"

    def card(p):
        tint = f' style="background:{p["tint"]}"' if p.get("tint") else ""
        href = f"produkt-{p['slug']}.html"
        return f"""
  <article class="product-card reveal">
    <a class="thumb" href="{href}"{tint}><img src="{img(p)}" alt="{p['title']}" loading="lazy"></a>
    <h3><a href="{href}">{p['title']}</a></h3>
    <p class="price">{p['price']}</p>
    <button class="btn" type="button" data-demo="{u('demo')}">{u('add')}</button>
  </article>"""

    h = lambda key: HOME[key][lang]
    benefits = "".join(f'<li class="reveal"><h3>{b[lang][0]}</h3><p>{b[lang][1]}</p></li>' for b in BENEFITS)
    ingredients = "".join(f'<li><span>{i}</span><div><h3>{x[lang][0]}</h3><p>{x[lang][1]}</p></div></li>' for i, x in enumerate(INGREDIENTS, 1))
    page(lang, "index.html", h("title"), u("subtitle"), f"""
<section class="hero">
  <div class="reveal">
    <h1>{h('h1')}</h1>
    <p class="lede">{h('lede')}</p>
    <div class="actions">
      <a class="btn btn-red" href="butikk.html">{h('shop')}</a>
      <a class="btn" href="bedrift.html">{u('business')}</a>
    </div>
  </div>
  <div class="hero-photo reveal">
    <img src="{up}assets/integrale2-1536x1152.jpg" alt="Scrocchia 80 pizza">
    <span class="hero-badge">{h('badge')}</span>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="head-row reveal">
    <div><p class="eyebrow">Shop</p><h2 class="title">{u('choose')}</h2></div>
    <a class="btn" href="butikk.html">{u('all_products')}</a>
  </div>
  <div class="products">{''.join(card(p) for p in PRODUCTS[:4])}
  </div>
</section>

<section class="section craft">
  <img class="reveal" src="{up}assets/pizza-la-classica-1403x1536.jpeg" alt="Scrocchia 80 pizza base" loading="lazy">
  <div class="reveal">
    <p class="eyebrow">{h('why')}</p>
    <h2 class="title">{h('craft')}</h2>
    <p class="lede">{h('craft_text')}</p>
    <strong>{h('success')}</strong>
    <div class="actions"><a class="btn" href="om-oss.html">{h('more')}</a></div>
  </div>
</section>

<section class="section">
  <div class="head-row reveal"><h2 class="title">{h('benefits')}</h2></div>
  <ul class="benefits">{benefits}</ul>
</section>

<section class="section ingredients">
  <div class="media reveal"><video data-lazy="{up}assets/hero-540.mp4" muted loop playsinline poster="{up}assets/og.jpg" aria-hidden="true"></video></div>
  <div class="reveal">
    <p class="eyebrow">{h('ing_eye')}</p>
    <h2 class="title">{h('ing_title')}</h2>
    <p class="lede">{h('ing_text')}</p>
    <ol class="ingredient-list">{ingredients}</ol>
    <p class="closing">{h('closing')}</p>
  </div>
</section>
""")

    page(lang, "butikk.html", "Shop – Scrocchia 80", u("subtitle"), f"""
<header class="page-head reveal"><h1>Shop</h1><p class="lede">{u('notice')}</p></header>
<section class="shop-grid"><div class="products">{''.join(card(p) for p in PRODUCTS)}
</div></section>
""", "butikk.html")

    for p in PRODUCTS:
        tint = f' style="background:{p["tint"]}"' if p.get("tint") else ""
        figures = "".join(f'<figure{tint}><img src="{img(p, i)}" alt="{p["title"]}"></figure>' for i in p["images"])
        specs = "".join(f"<div><dt>{K[k][lang]}</dt><dd>{v[lang]}</dd></div>" for k, v in p["specs"])
        intro = "".join(f"<p>{t[lang]}</p>" for t in p["intro"])
        tag = p.get("tag")
        tag = tag[lang] if isinstance(tag, dict) else tag
        n = p["reviews"]
        reviews = f'<p class="reviews">{n} {u("reviews1") if n == 1 else u("reviewsN")}</p>' if n else ""
        sub = f'<p class="reviews">{p["subtitle"][lang]}</p>' if p.get("subtitle") else ""
        doc = f'<a class="doc-link" href="{p["doc"][0]}" target="_blank" rel="noopener noreferrer">{p["doc"][1]}</a>' if p.get("doc") else ""
        page(lang, f"produkt-{p['slug']}.html", f"{p['title']} – Scrocchia 80", p["intro"][0][lang][:150], f"""
<section class="product">
  <div class="gallery reveal{' three' if len(p['images']) == 4 else ''}">{figures}</div>
  <div class="product-info reveal">
    <a class="back" href="butikk.html">{u('back')}</a>
    {f'<p class="eyebrow">{tag}</p>' if tag else ''}
    <h1>{p['title']}</h1>
    {sub}
    <p class="price">{p['price']}</p>
    {reviews}
    <div class="intro">{intro}</div>
    <div class="actions"><button class="btn btn-red" type="button" data-demo="{u('demo')}">{u('add')}</button></div>
    {f'<dl class="specs">{specs}</dl>' if specs else ''}
    {doc}
  </div>
</section>
""", "butikk.html")

    a = lambda key: ABOUT[key][lang]
    para = lambda items: "".join(f"<p>{x}</p>" for x in items)
    team = "".join(f'<img class="reveal" src="{up}assets/team-p{n}.jpg" alt="Scrocchia 80 team" loading="lazy">' for n in (1, 3, 5, 2, 4, 6))
    page(lang, "om-oss.html", f"{u('about')} – Scrocchia 80", a("welcome"), f"""
<header class="page-head reveal"><p class="eyebrow">{u('about')}</p><h1 style="margin-top:.9rem">{a('welcome')}</h1></header>
<section class="about-grid">
  <div class="block reveal"><h2>{a('h2a')}</h2>{para(a('a'))}</div>
  <div class="block reveal"><h2>{a('h2b')}</h2>{para(a('b'))}</div>
</section>
<section class="team" aria-label="Team">{team}</section>
<section class="section pull"><blockquote class="reveal">{a('quote')}</blockquote></section>
""", "om-oss.html")

    b = lambda key: BIZ[key][lang]
    page(lang, "bedrift.html", f"{u('business')} – Scrocchia 80", b("eye"), f"""
<header class="page-head reveal"><p class="eyebrow">{b('eye')}</p><h1 style="margin-top:.9rem">{u('business')}</h1></header>
<section class="business">
  <div class="copy reveal">
    <p class="lede">{b('lede')}</p>
    <p style="margin-top:1.25rem">{b('p1')}</p>
    <p>{b('p2')}</p>
  </div>
  <form class="form reveal">
    <label class="field"><span>{b('first')}</span><input name="first" required autocomplete="given-name"></label>
    <label class="field"><span>{b('last')}</span><input name="last" required autocomplete="family-name"></label>
    <label class="field"><span>{b('company')}</span><input name="company" required autocomplete="organization"></label>
    <label class="field"><span>{b('orgnr')}</span><input name="org" required></label>
    <label class="field full"><span>{u('email')} *</span><input name="email" type="email" required autocomplete="email"></label>
    <label class="field full"><span>{b('subject')}</span><input name="subject" required></label>
    <label class="field full"><span>{b('msg')}</span><textarea name="message" rows="5"></textarea></label>
    <div><button class="btn btn-red" type="submit">{b('send')}</button></div>
    <p class="form-note" role="status"></p>
  </form>
</section>
""", "bedrift.html")


for language in LANGS:
    build(language)
