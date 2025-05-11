# 🦸‍♂️ Polymorphism Challenge! 🎭

Welcome to the **Polymorphism Challenge** in Python! This simple project demonstrates the power of **polymorphism** and **inheritance** through fun and creative examples like millipedes, dolphins, and superheroes.

---

## 🚀 Features

### 🐛 `Millipede` and 🐬 `Dolphin`
These two classes both implement a `.move()` method but behave differently, showcasing **polymorphism** — the ability to call the same method name on different objects and get behavior specific to the object's class.

```python
millipede = Millipede()
print(millipede.move())  # Output: Crawling.

dolphin = Dolphin()
print(dolphin.move())    # Output: Swimming.