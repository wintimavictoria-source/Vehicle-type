class Vehicle:
    def __init__(self):
        self.vehicle_type = None
        self.brand = None
        self.model = None
        self.wheels = 4
        self.engine = None
        self.color = "White"
        self.features = []

    def __str__(self):
        features_str = ", ".join(self.features) if self.features else "None"
        return (
            f"--- {self.color} {self.brand} {self.model} ({self.vehicle_type}) ---\n"
            f"Wheels: {self.wheels}\n"
            f"Engine: {self.engine}\n"
            f"Features: {features_str}"
        )

class VehicleBuilder:
    def __init__(self):
        self.vehicle = Vehicle()

    def set_type(self, v_type: str):
        self.vehicle.vehicle_type = v_type
        return self

    def set_brand_and_model(self, brand: str, model: str):
        self.vehicle.brand = brand
        self.vehicle.model = model
        return self

    def set_wheels(self, count: int):
        self.vehicle.wheels = count
        return self

    def set_engine(self, engine: str):
        self.vehicle.engine = engine
        return self

    def set_color(self, color: str):
        self.vehicle.color = color
        return self

    def add_feature(self, feature: str):
        self.vehicle.features.append(feature)
        return self

    def build(self):
        return self.vehicle

# Usage example:
builder = VehicleBuilder()
my_car = (
    builder.set_type("Car")
    .set_brand_and_model("Toyota", "Camry")
    .set_wheels(4)
    .set_engine("V6 Petrol")
    .set_color("Midnight Blue")
    .add_feature("Sunroof")
    .add_feature("Leather Seats")
    .build()
)

print(my_car)
