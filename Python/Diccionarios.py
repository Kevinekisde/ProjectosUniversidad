#MLB_TEAM={
    #"colorado":"rockies"
    #"boston":"red sox"
    #"minnesota":"twins"
    #"milwaukee":"brewers"
    #"seatle":"mariners"#}

MLB_TEAM=dict([
    "colorado":"rockies"
    "boston": "red sox"
    "minnesota":"twins"
    "milwaukee":"brewers"
    "seatle":"mariners"
    ])

MLB_TEAM=dict(
    colorado= "rockies"
    boston= "red sox"
    minnesota="twins"
    milwaukee="brewers"
    seatle="mariners"
)

#### BUSCAR ELEMENTOS

print(MLB_TEAM("minnesota"))

#### AÑADIR

MLB_TEAM["kansas city"]="royals"

### ELIMINIAR

del MLB_TEAM["seatle"]