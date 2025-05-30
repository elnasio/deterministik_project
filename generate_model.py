from app.ml_model import SimpleMLP

model = SimpleMLP(input_size=5, output_size=5)
model.save("model.npz")

print("✅ Dummy model saved to model.npz")
