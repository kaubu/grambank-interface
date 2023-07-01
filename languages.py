frisian = {
    "west2354": {
        "name": "Western Frisian",
    },
}

anglic = {
    "stan1293": {
        "name": "English",
    },
    # Scots – There is no Scots language code
}

# Anglo-Frisian
anglo_frisian = anglic | frisian

dutch = {
    "dutc1256": {
        "name": "Dutch",
    },
}

# Low Franconian
low_franconian = dutch

## West Germanic
west_germanic = anglo_frisian | low_franconian

# North-West Germanic
north_west_germanic = {
    "icel1247": {
        "name": "Icelandic",
    },
    "faro1244": {
        "name": "Faroese",
    },
    # Norwegian. No Norwegian data
}

# North-East Germanic
north_east_germanic = {
    "dani1285": {
        "name": "Danish",
    },
    "swed1254": {
        "name": "Swedish",
    },
}

## North Germanic
north_germanic = north_west_germanic | north_east_germanic

# Hellenic
hellenic = {
    # "anci1242": {
    #     "name": "Ancient Greek",
    # }, # Commented because it's dead
    "mode1248": {
        "name": "Modern Greek",
    },
}

test = {
    "cent2127": {
        "name": "Central Alaskan Yupik",
    }
}

living_indo_european = {
    "arom1237": {
        "name": "Aromanian",
        "native_speakers": 210000,
        "total_speakers": 210000,
        "native_weight": 0.01096072713948203,
        "total_weight": 0.006385397257634067
    },
    "awad1243": {
        "name": "Awadhi",
        "native_speakers": 4400000,
        "total_speakers": 4400000,
        "native_weight": 0.22965333054152828,
        "total_weight": 0.1337892758742376
    },
    "baha1260": {
        "name": "Bahamas Creole English / Bahamas Creole",
        "native_speakers": 400000,
        "total_speakers": 400000,
        "native_weight": 0.020877575503775295,
        "total_weight": 0.012162661443112508
    },
    "bela1254": {
        "name": "Belarusian",
        "native_speakers": 5100000,
        "total_speakers": 11400000,
        "native_weight": 0.26618908767313504,
        "total_weight": 0.3466358511287065
    },
    "beli1260": {
        "name": "Belize Kriol English / Belizean Creole",
        "native_speakers": 150000,
        "total_speakers": 350000,
        "native_weight": 0.007829090813915737,
        "total_weight": 0.010642328762723445
    },
    "bhoj1244": {
        "name": "Bhojpuri",
        "native_speakers": 51000000,
        "total_speakers": 51000000,
        "native_weight": 2.6618908767313503,
        "total_weight": 1.550739333996845
    },
    "bisl1239": {
        "name": "Bislama",
        "native_speakers": 10000,
        "total_speakers": 210000,
        "native_weight": 0.0005219393875943825,
        "total_weight": 0.006385397257634067
    },
    "bret1244": {
        "name": "Breton",
        "native_speakers": 226000,
        "total_speakers": 226000,
        "native_weight": 0.011795830159633043,
        "total_weight": 0.006871903715358567
    },
    "bund1253": {
        "name": "Bundeli",
        "native_speakers": 5600000,
        "total_speakers": 5600000,
        "native_weight": 0.29228605705285415,
        "total_weight": 0.17027726020357511
    },
    "camp1261": {
        "name": "Campidanese Sardinian",
        "native_speakers": 500000,
        "total_speakers": 500000,
        "native_weight": 0.02609696937971912,
        "total_weight": 0.015203326803890634
    },
    "cent1972": {
        "name": "Central Kurdish / Sorani Kurdish",
        "native_speakers": 8000000,
        "total_speakers": 8000000,
        "native_weight": 0.4175515100755059,
        "total_weight": 0.24325322886225015
    },
    "cors1241": {
        "name": "Corsican",
        "native_speakers": 150000,
        "total_speakers": 150000,
        "native_weight": 0.007829090813915737,
        "total_weight": 0.0045609980411671905
    },
    "czec1258": {
        "name": "Czech",
        "native_speakers": 10700000,
        "total_speakers": 10700000,
        "native_weight": 0.5584751447259892,
        "total_weight": 0.32535119360325965
    },
    "dani1285": {
        "name": "Danish",
        "native_speakers": 6000000,
        "total_speakers": 6000000,
        "native_weight": 0.31316363255662943,
        "total_weight": 0.18243992164668763
    },
    "dara1250": {
        "name": "Darai / Bote-Darai",
        "native_speakers": 20000,
        "total_speakers": 20000,
        "native_weight": 0.001043878775188765,
        "total_weight": 0.0006081330721556254
    },
    "doma1260": {
        "name": "Domaaki / Dawoodi",
        "native_speakers": 340,
        "total_speakers": 340,
        "native_weight": 1.7745939178209002e-05,
        "total_weight": 1.0338262226645632e-05
    },
    "dutc1256": {
        "name": "Dutch",
        "native_speakers": 25000000,
        "total_speakers": 30000000,
        "native_weight": 1.304848468985956,
        "total_weight": 0.912199608233438
    },
    "faro1244": {
        "name": "Faroese",
        "native_speakers": 72000,
        "total_speakers": 72000,
        "native_weight": 0.003757963590679554,
        "total_weight": 0.0021892790597602516
    },
    "gali1258": {
        "name": "Galician",
        "native_speakers": 2400000,
        "total_speakers": 2400000,
        "native_weight": 0.1252654530226518,
        "total_weight": 0.07297596865867505
    },
    "gheg1238": {
        "name": "Gheg Albanian",
        "native_speakers": 4100000,
        "total_speakers": 4100000,
        "native_weight": 0.2139951489136968,
        "total_weight": 0.12466727979190322
    },
    "gura1251": {
        "name": "Gurani / Gorani",
        "native_speakers": 350000,
        "total_speakers": 350000,
        "native_weight": 0.018267878565803385,
        "total_weight": 0.010642328762723445
    },
    "hait1244": {
        "name": "Haitian / Haitian Creole",
        "native_speakers": 12000000,
        "total_speakers": 12000000,
        "native_weight": 0.6263272651132589,
        "total_weight": 0.36487984329337525
    },
    "hind1269": {
        "name": "Hindi",
        "native_speakers": 322000000,
        "total_speakers": 592000000,
        "native_weight": 16.80644828053911,
        "total_weight": 18.000738935806513
    },
    "icel1247": {
        "name": "Icelandic",
        "native_speakers": 357069,
        "total_speakers": 357069,
        "native_weight": 0.01863683751889385,
        "total_weight": 0.010857273397076851
    },
    "iris1253": {
        "name": "Irish",
        "native_speakers": 170000,
        "total_speakers": 2272597,
        "native_weight": 0.008872969589104501,
        "total_weight": 0.0691020697690829
    },
    "iron1242": {
        "name": "Iron Ossetian",
        "native_speakers": 511958,
        "total_speakers": 511958,
        "native_weight": 0.026721104499404486,
        "total_weight": 0.015566929567732484
    },
    "ital1282": {
        "name": "Italian",
        "native_speakers": 65000000,
        "total_speakers": 68100000,
        "native_weight": 3.3926060193634857,
        "total_weight": 2.0706931106899047
    },
    "jama1262": {
        "name": "Jamaican Creole English / Jamaian Patois",
        "native_speakers": 3200000,
        "total_speakers": 3200000,
        "native_weight": 0.16702060403020236,
        "total_weight": 0.09730129154490007
    },
    "kash1277": {
        "name": "Kashmiri",
        "native_speakers": 7100000,
        "total_speakers": 7100000,
        "native_weight": 0.37057696519201155,
        "total_weight": 0.21588724061524703
    },
    "konk1267": {
        "name": "Konkan Marathi / Maharashtri Konkani",
        "native_speakers": 2400000,
        "total_speakers": 2400000,
        "native_weight": 0.1252654530226518,
        "total_weight": 0.07297596865867505
    },
    "kumz1235": {
        "name": "Kumzari",
        "native_speakers": 6030,
        "total_speakers": 6030,
        "native_weight": 0.0003147294507194126,
        "total_weight": 0.00018335212125492105
    },
    "lamb1269": {
        "name": "Lambadi",
        "native_speakers": 5000000,
        "total_speakers": 5000000,
        "native_weight": 0.2609696937971912,
        "total_weight": 0.15203326803890635
    },
    "latv1249": {
        "name": "Latvian",
        "native_speakers": 1500000,
        "total_speakers": 1500000,
        "native_weight": 0.07829090813915736,
        "total_weight": 0.045609980411671906
    },
    "limo1249": {
        "name": "Limonese Creole",
        "native_speakers": 55000,
        "total_speakers": 55000,
        "native_weight": 0.0028706666317691036,
        "total_weight": 0.00167236594842797
    },
    "lith1251": {
        "name": "Lithuanian",
        "native_speakers": 3000000,
        "total_speakers": 3000000,
        "native_weight": 0.15658181627831472,
        "total_weight": 0.09121996082334381
    },
    "lomb1257": {
        "name": "Lombard",
        "native_speakers": 3800000,
        "total_speakers": 3800000,
        "native_weight": 0.19833696728586533,
        "total_weight": 0.11554528370956883
    },
    "mace1250": {
        "name": "Macedonian",
        "native_speakers": 3500000,
        "total_speakers": 3500000,
        "native_weight": 0.18267878565803383,
        "total_weight": 0.10642328762723444
    },
    "maga1260": {
        "name": "Magahi",
        "native_speakers": 12600000,
        "total_speakers": 12600000,
        "native_weight": 0.6576436283689219,
        "total_weight": 0.383123835458044
    },
    "mait1250": {
        "name": "Maithili",
        "native_speakers": 34000000,
        "total_speakers": 34000000,
        "native_weight": 1.7745939178209003,
        "total_weight": 1.0338262226645631
    },
    "mara1378": {
        "name": "Marathi",
        "native_speakers": 83000000,
        "total_speakers": 95000000,
        "native_weight": 4.3320969170333745,
        "total_weight": 2.8886320927392206
    },
    "mode1248": {
        "name": "Modern Greek",
        "native_speakers": 13400000,
        "total_speakers": 13400000,
        "native_weight": 0.6993987793764724,
        "total_weight": 0.40744915834426904
    },
    "nepa1254": {
        "name": "Nepali",
        "native_speakers": 16000000,
        "total_speakers": 25000000,
        "native_weight": 0.8351030201510118,
        "total_weight": 0.7601663401945318
    },
    "nica1252": {
        "name": "Nicaragua Creole English / Miskito Coast Creole",
        "native_speakers": 18000,
        "total_speakers": 18000,
        "native_weight": 0.0009394908976698885,
        "total_weight": 0.0005473197649400629
    },
    "nucl1235": {
        "name": "Eastern Armenian",
        "native_speakers": 3800000,
        "total_speakers": 3800000,
        "native_weight": 0.19833696728586533,
        "total_weight": 0.11554528370956883
    },
    "occi1239": {
        "name": "Occitan",
        "native_speakers": 200000,
        "total_speakers": 800000,
        "native_weight": 0.010438787751887647,
        "total_weight": 0.024325322886225017
    },
    "oriy1255": {
        "name": "Odia",
        "native_speakers": 35000000,
        "total_speakers": 39000000,
        "native_weight": 1.8267878565803384,
        "total_weight": 1.1858594907034696
    },
    "panj1256": {
        "name": "Eastern Panjabi / Standard Punjabi",
        "native_speakers": 113000000,
        "total_speakers": 113000000,
        "native_weight": 5.897915079816522,
        "total_weight": 3.4359518576792833
    },
    "piji1239": {
        "name": "Pijin",
        "native_speakers": 24000,
        "total_speakers": 324000,
        "native_weight": 0.0012526545302265178,
        "total_weight": 0.009851755768921132
    },
    "plau1238": {
        "name": "Plautdietsch",
        "native_speakers": 450000,
        "total_speakers": 450000,
        "native_weight": 0.02348727244174721,
        "total_weight": 0.013682994123501572
    },
    "poli1260": {
        "name": "Polish",
        "native_speakers": 40000000,
        "total_speakers": 45000000,
        "native_weight": 2.0877575503775296,
        "total_weight": 1.3682994123501573
    },
    "port1283": {
        "name": "Portuguese",
        "native_speakers": 230000000,
        "total_speakers": 260000000,
        "native_weight": 12.004605914670796,
        "total_weight": 7.90572993802313
    },
    "pras1239": {
        "name": "Prasun / Wasi-wari",
        "native_speakers": 8000,
        "total_speakers": 8000,
        "native_weight": 0.00041755151007550587,
        "total_weight": 0.00024325322886225017
    },
    "roma1326": {
        "name": "Romansh",
        "native_speakers": 40000,
        "total_speakers": 60000,
        "native_weight": 0.00208775755037753,
        "total_weight": 0.0018243992164668763
    },
    "russ1263": {
        "name": "Russian",
        "native_speakers": 150000000,
        "total_speakers": 260000000,
        "native_weight": 7.829090813915736,
        "total_weight": 7.90572993802313
    },
    "sana1297": {
        "name": "San Andres Creole English / San Andrés—Providencia creole",
        "native_speakers": 12000,
        "total_speakers": 12000,
        "native_weight": 0.0006263272651132589,
        "total_weight": 0.00036487984329337526
    },
    "sara1340": {
        "name": "Saramaccan",
        "native_speakers": 90000,
        "total_speakers": 90000,
        "native_weight": 0.004697454488349442,
        "total_weight": 0.0027365988247003144
    },
    "sici1248": {
        "name": "Sicilian",
        "native_speakers": 4700000,
        "total_speakers": 4700000,
        "native_weight": 0.24531151216935976,
        "total_weight": 0.14291127195657197
    },
    "slov1268": {
        "name": "Slovenian / Slovene",
        "native_speakers": 2500000,
        "total_speakers": 2500000,
        "native_weight": 0.1304848468985956,
        "total_weight": 0.07601663401945317
    },
    "sout1528": {
        "name": "Serbian-Croatian-Bosnian / Serbo-Croatian",
        "native_speakers": 19000000,
        "total_speakers": 19000000,
        "native_weight": 0.9916848364293266,
        "total_weight": 0.5777264185478441
    },
    "sout2649": {
        "name": "Southern Pashto",
        "native_speakers": 16893700,
        "total_speakers": 16893700,
        "native_weight": 0.8817487432203218,
        "total_weight": 0.5136808840537745
    },
    "stan1289": {
        "name": "Catalan",
        "native_speakers": 4100000,
        "total_speakers": 9200000,
        "native_weight": 0.2139951489136968,
        "total_weight": 0.27974121319158773
    },
    "stan1290": {
        "name": "French",
        "native_speakers": 80000000,
        "total_speakers": 270000000,
        "native_weight": 4.175515100755059,
        "total_weight": 8.209796474100942
    },
    "stan1293": {
        "name": "English",
        "native_speakers": 372900000,
        "total_speakers": 1080000000,
        "native_weight": 19.46311976339452,
        "total_weight": 32.83918589640377
    },
    "swed1254": {
        "name": "Swedish",
        "native_speakers": 10000000,
        "total_speakers": 13000000,
        "native_weight": 0.5219393875943824,
        "total_weight": 0.39528649690115647
    },
    "tokp1240": {
        "name": "Tok Pisin",
        "native_speakers": 130000,
        "total_speakers": 4130000,
        "native_weight": 0.006785212038726972,
        "total_weight": 0.12557947940013667
    },
    "torr1261": {
        "name": "Torres Strait-Lockhart River Creole / Torres Strait Creole",
        "native_speakers": 30000,
        "total_speakers": 30000,
        "native_weight": 0.0015658181627831473,
        "total_weight": 0.0009121996082334382
    },
    "tosk1239": {
        "name": "Northern Tosk Albanian",
        "native_speakers": 1800000,
        "total_speakers": 1800000,
        "native_weight": 0.09394908976698883,
        "total_weight": 0.05473197649400629
    },
    "ukra1253": {
        "name": "Ukrainian",
        "native_speakers": 27000000,
        "total_speakers": 32800000,
        "native_weight": 1.4092363465048325,
        "total_weight": 0.9973382383352257
    },
    "wels1247": {
        "name": "Welsh",
        "native_speakers": 657185,
        "total_speakers": 657185,
        "native_weight": 0.03430107364362142,
        "total_weight": 0.019982796651229734
    },
    "west2354": {
        "name": "Western Frisian / West Frisian",
        "native_speakers": 470000,
        "total_speakers": 470000,
        "native_weight": 0.024531151216935974,
        "total_weight": 0.014291127195657196
    },
    "west2369": {
        "name": "Western Farsi / Iranian Persian",
        "native_speakers": 55600000,
        "total_speakers": 55600000,
        "native_weight": 2.9019829950247664,
        "total_weight": 1.6906099405926387
    },
    "west2386": {
        "name": "Western Panjabi",
        "native_speakers": 34520000,
        "total_speakers": 34520000,
        "native_weight": 1.801734765975808,
        "total_weight": 1.0496376825406095
    }
}