# master_thesis

This application was developed as part of the master's thesis "Entwicklung einer Applikation zur Bestimmung von Nährwerten in Fotos von Mahlzeiten" ("Development of an Application for Determining Nutritional Values from Meal Photos") and identifies 101 dishes from the Food-101 dataset. The ResNet model used for food identification was trained separately, saved, and loaded into this repository.

Once a dish is identified, the corresponding ingredients are assigned to it, and the calories and nutritional values are displayed per 100g.

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Start Flask Server

```sh
python app.py
```

```sh
npm run lint
```
