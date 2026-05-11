# dict of names
ENEMY_NAMES = {
    "ogre": ("Ozar", "Ozag", "Burag", "Druzur", "Xuzor", "Vegigark", "Blaukig", "Blanikork", "Kusazug", "Yuwukork", "Mogur", "Grakug", "Zurog", "Brakar", "Vogthak", "Drazg", "Krolug", "Thrazag", "Gromm", "Urkeg", "Ruzok", "Balthog", "Glurg", "Mazzug", "Trogak", "Vargak", "Drogul", "Zark", "Kruglak", "Grotth", "Buzak", "Hogar", "Thok", "Razgug", "Mungog", "Gruk", "Zog", "Dreg", "Brogh", "Kraz"),
    "thug": ("Brick", "Rick", "Ivan", "Dmitriy", "John", "Joe", "Skinny", "Tall", "Doc", "Hammer", "Jacket", "Steve", "Bill", "Bone", "Jack", "Viktor", "Stan", "Mick", "Frank", "Anton", "Shorty", "Slim", "Tiny", "Biggs", "Red", "Dutch", "Sawyer", "Axel", "Clutch", "Patch", "Spike", "Miller", "Flint", "Steel", "Butch", "Duke", "Knuckles", "Cage"),
    "cultist": ("Malphas", "Xarros", "Vane", "Kael", "Morthos", "Mordekai", "Scythe", "Zealot", "Acolyte", "Brother Night", "Sister Void", "Father Doom", "Malakor", "Dread", "Zalros", "Nyx", "Umbra", "Cipher", "Bane", "Arkon", "Belial", "Vex", "Obsidian", "Sorrow", "Hollow", "Vesper", "Sanguine", "Prophet", "Disciple", "Omen", "Relic", "Curse", "Blight", "Abyss", "Grim", "Sigil", "Rune", "Ether", "Solace", "Gloom"),
    "mercenary": ("Viper", "Ghost", "Reaper", "Bishop", "Zero", "Echo", "Sarge", "Gunner", "Kilo", "Sabre", "Hunter", "Falcon", "Wolf", "Ajax", "Nomad", "Titan", "Raptor", "Stryker", "Odin", "Goliath", "Bane", "Ronin", "Hedge", "Sledge", "Talon", "Breaker", "Wardog", "Maverick", "Colt", "Steel", "Jester", "Vanguard", "Rogue", "Outlaw", "Flint", "Trace", "Vortex", "Slayer", "Major", "Shield"),
    "ghoul": ("Rot", "Gnasher", "Carrion", "Skitter", "Pale", "Fester", "Marrow", "Shambler", "Grip", "Lurker", "Bile", "Gristle", "Sliver", "Crawler", "Rags", "Jaw", "Gut", "Wretch", "Blight", "Corpse", "Snapper", "Grimace", "Sludge", "Hollow", "Twitch", "Gibber", "Flay", "Retch", "Mangler", "Shred", "Vile", "Scrapper", "Howler", "Clicker", "Gore", "Dreg", "Waste", "Pox", "Cadaver", "Slink"),
    "foreign_soldier": ("Kovacs", "Miller", "Schmidt", "Petrov", "Volkov", "Chen", "Sato", "Wagner", "Rossi", "Dubois", "Hassan", "Diaz", "Silva", "Andersson", "Novak", "Larsen", "Kim", "Lee", "Park", "Grant", "Fisher", "Stone", "Cross", "Black", "Steele", "Mason", "Wolf", "Hunter", "Becker", "Horton", "Dixon", "Price", "Vance", "Reid", "Hayes", "Foster", "Brooks", "Banks", "Kelly", "Ward")
}

# dict of descriptions
ENEMY_DESCRIPTIONS = {
    "thug": (
        "An amateur looking for an easy target.",
        "A street-tough with a mean streak.",
        "A seasoned brawler who knows how to hurt you.",
        "A brutal enforcer covered in scars.",
        "A legendary kingpin of the local underworld."
    ),
    "ogre": (
        "A small, stunted brute with a dull club.",
        "A lumbering beast with thick, leathery skin.",
        "A massive wall of muscle and bad attitude.",
        "A hulking monster wearing scrap-metal armor.",
        "A mountain-sized titan that shakes the earth."
    ),
    "snake": (
        "A tiny garden serpent with a weak hiss.",
        "A thick constrictor looking for a meal.",
        "A hooded cobra dripping with fresh venom.",
        "A massive python capable of crushing bone.",
        "A prehistoric giant that could swallow a man whole."
    ),
    "wolf": (
        "A scrawny pup driven by hunger.",
        "A lone hunter patrolling its territory.",
        "A sleek predator with razor-sharp teeth.",
        "An alpha male, scarred and battle-tested.",
        "A monstrous dire-wolf with eyes of cold fire."
    ),
    "skeleton": (
        "A pile of rattling bones barely held together.",
        "An animated corpse clutching a rusted blade.",
        "A skeletal warrior in rotting leather armor.",
        "A hollow-eyed knight of a forgotten age.",
        "A lich-guard wreathed in flickering soul-fire."
    ),
    "zombie": (
        "A slow, rotting corpse stumbling aimlessly.",
        "A fresh cadaver with surprising grip strength.",
        "A bloated horror that refuses to go down.",
        "A decaying soldier clumsily gripping a rusted pistol.",
        "A relentless 'Shambler' mindlessly firing a submachine gun."
    ),
    "cultist": (
        "A wide-eyed initiate chanting nervously.",
        "A devoted follower with a sharpened ritual knife.",
        "A fanatical zealot with a blood-stained robe.",
        "A high priest channeling dark, forbidden whispers.",
        "An avatar of the cult, glowing with eerie energy."
    ),
    "ghoul": (
        "A starving scavenger picking at scraps.",
        "A pale, twitching creature with jagged claws.",
        "A fast-moving lurker that smells of rot.",
        "A feral hunter that has tasted human flesh.",
        "A 'Grave-Lord'—faster and deadlier than any man."
    ),
    "mercenary": (
        "A hired hand with cheap gear and low morale.",
        "A professional soldier working for the highest bidder.",
        "A tactical specialist with reinforced armor.",
        "A cold-blooded assassin who never misses.",
        "A legendary 'War-Dog' who has survived a dozen wars."
    ),
    "foreign_soldier": (
        "A young conscript far from home.",
        "A disciplined infantryman in standard uniform.",
        "An elite scout trained in hostile environments.",
        "A high-ranking officer with advanced weaponry.",
        "A special-ops commando from a distant empire."
    )
}