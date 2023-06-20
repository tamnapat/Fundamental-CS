products = [
        {"code": "CM-112", "name": "CardioMax Jump Rope", "price": 14.99},
        {"code": "HM-113", "name": "HydrateMate Water Bottle", "price": 19.99},
        {"code": "PB-114", "name": "PowerBeam LED Headlamp", "price": 24.99},
        {"code": "PF-115", "name": "ProFit Pilates Ring", "price": 19.99},
        {"code": "AF-116", "name": "AeroFlow Compression Socks", "price": 17.99},
        {"code": "AG-117", "name": "AquaGuard Waterproof Phone Case", "price": 12.99},
        {"code": "GM-118", "name": "GripMaster Hand Exerciser", "price": 14.99},
        {"code": "SP-119", "name": "SportPlus Yoga Mat", "price": 29.99},
        {"code": "AG-120", "name": "AeroGlide Foam Roller", "price": 29.99},
        {"code": "CP-121", "name": "CorePower Ab Roller", "price": 19.99},
        {"code": "FB-122", "name": "FitBreeze Running Socks", "price": 9.99},
        {"code": "UH-123", "name": "UltraHeat Heating Pad", "price": 24.99}
        ]

s = input("Product code: ")

for i in products:
    if s == i["code"]:
        print("")
        print("Product name:", i["name"])
        print("Product price:", i["price"])
