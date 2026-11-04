
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="What's in My Fridge?",
    page_icon="🥑",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #000000;
    color: #FFFFFF;
}

/* All text */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp p,
.stApp label,
.stApp span,
.stApp li,
.stApp .stMarkdown {
    color: #FFFFFF !important;
}

/* Main title */
.main-title {
    color: #FFFFFF !important;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

/* Subtitle */
.subtitle {
    color: #FFFFFF !important;
    text-align: center;
    font-size: 17px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111111;
}

/* Input fields */
.stTextInput input,
.stMultiSelect,
.stSelectbox div[data-baseweb="select"] {
    background-color: #222222;
    color: #FFFFFF;
}

/* Dropdown options */
div[data-baseweb="popover"],
div[data-baseweb="menu"] {
    background-color: #222222;
    color: #FFFFFF;
}

/* Recipe cards */
.recipe-card {
    background-color: #151515;
    color: #FFFFFF;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #333333;
}

/* Buttons */
div.stButton > button {
    background-color: #198754;
    color: #FFFFFF !important;
    border-radius: 10px;
    border: none;
}

/* Button hover */
div.stButton > button:hover {
    background-color: #28A745;
    color: #FFFFFF !important;
}

/* Metrics */
[data-testid="stMetricValue"],
[data-testid="stMetricLabel"] {
    color: #FFFFFF !important;
}

/* Expanders */
.streamlit-expanderHeader {
    color: #FFFFFF !important;
}

/* Divider */
hr {
    border-color: #444444;
}

</style>
""", unsafe_allow_html=True)



# ---------------- RECIPE DATABASE ----------------

recipes = [

    {
        "name": "Cheese Omelette",
        "category": "Vegetarian",
        "time": 15,
        "difficulty": "Easy",
        "emoji": "🍳",
        "ingredients": [
            "eggs", "cheese", "onion", "salt"
        ],
        "instructions": [
            "Crack eggs into a bowl.",
            "Add chopped onion and salt.",
            "Beat everything together.",
            "Heat a pan with a little oil.",
            "Pour the egg mixture into the pan.",
            "Add cheese and cook until ready."
        ]
    },

    {
        "name": "Vegetable Sandwich",
        "category": "Vegetarian",
        "time": 10,
        "difficulty": "Easy",
        "emoji": "🥪",
        "ingredients": [
            "bread", "tomato", "onion", "cheese"
        ],
        "instructions": [
            "Take two slices of bread.",
            "Cut tomato and onion into slices.",
            "Add cheese and vegetables.",
            "Place everything between bread slices.",
            "Toast if you prefer."
        ]
    },

    {
        "name": "Tomato Pasta",
        "category": "Vegetarian",
        "time": 25,
        "difficulty": "Medium",
        "emoji": "🍝",
        "ingredients": [
            "pasta", "tomato", "garlic", "salt", "cheese"
        ],
        "instructions": [
            "Boil pasta in salted water.",
            "Chop tomatoes and garlic.",
            "Cook garlic and tomatoes in a pan.",
            "Add salt and cooked pasta.",
            "Mix everything together.",
            "Add cheese before serving."
        ]
    },

    {
        "name": "Chicken Sandwich",
        "category": "Non-Vegetarian",
        "time": 20,
        "difficulty": "Easy",
        "emoji": "🥪",
        "ingredients": [
            "chicken", "bread", "onion", "tomato", "salt"
        ],
        "instructions": [
            "Cook chicken thoroughly with salt.",
            "Shred or cut the chicken.",
            "Slice tomato and onion.",
            "Place chicken and vegetables on bread.",
            "Serve your sandwich."
        ]
    },

    {
        "name": "Banana Smoothie",
        "category": "Vegetarian",
        "time": 5,
        "difficulty": "Easy",
        "emoji": "🥤",
        "ingredients": [
            "banana", "milk", "sugar"
        ],
        "instructions": [
            "Peel the banana.",
            "Add banana and milk to a blender.",
            "Add sugar if desired.",
            "Blend until smooth.",
            "Serve chilled."
        ]
    },

    {
        "name": "French Toast",
        "category": "Vegetarian",
        "time": 10,
        "difficulty": "Easy",
        "emoji": "🍞",
        "ingredients": [
            "bread", "eggs", "milk", "sugar"
        ],
        "instructions": [
            "Beat eggs and milk together.",
            "Add a little sugar.",
            "Dip bread slices into the mixture.",
            "Cook both sides in a pan.",
            "Serve warm."
        ]
    },

    {
        "name": "Chicken Fried Rice",
        "category": "Non-Vegetarian",
        "time": 25,
        "difficulty": "Medium",
        "emoji": "🍚",
        "ingredients": [
            "rice", "chicken", "eggs", "onion", "salt"
        ],
        "instructions": [
            "Cook chicken thoroughly.",
            "Prepare rice separately.",
            "Scramble eggs in a pan.",
            "Add onion and cooked chicken.",
            "Add rice and salt.",
            "Mix and cook until heated through."
        ]
    },

    {
        "name": "Potato Fries",
        "category": "Vegetarian",
        "time": 20,
        "difficulty": "Easy",
        "emoji": "🍟",
        "ingredients": [
            "potato", "salt", "oil"
        ],
        "instructions": [
            "Wash and peel potatoes.",
            "Cut potatoes into strips.",
            "Heat oil in a pan.",
            "Fry until golden and fully cooked.",
            "Add salt and serve."
        ]
    },

    {
        "name": "Fruit Salad",
        "category": "Vegetarian",
        "time": 10,
        "difficulty": "Easy",
        "emoji": "🥗",
        "ingredients": [
            "apple", "banana", "orange", "milk"
        ],
        "instructions": [
            "Wash all fruits.",
            "Cut fruits into small pieces.",
            "Place them in a bowl.",
            "Add milk if desired.",
            "Mix and serve fresh."
        ]
    },

    {
        "name": "Garlic Cheese Toast",
        "category": "Vegetarian",
        "time": 10,
        "difficulty": "Easy",
        "emoji": "🧀",
        "ingredients": [
            "bread", "cheese", "garlic", "butter"
        ],
        "instructions": [
            "Mix crushed garlic with butter.",
            "Spread the mixture on bread.",
            "Add cheese on top.",
            "Toast until the cheese melts.",
            "Serve warm."
        ]
    },

    {
        "name": "Chicken Curry",
        "category": "Non-Vegetarian",
        "time": 40,
        "difficulty": "Medium",
        "emoji": "🍗",
        "ingredients": [
            "chicken", "tomato", "onion", "garlic", "salt"
        ],
        "instructions": [
            "Heat oil in a cooking pot.",
            "Add chopped onion and garlic.",
            "Add tomato and cook until soft.",
            "Add chicken and seasonings.",
            "Cook until chicken is fully cooked.",
            "Serve hot."
        ]
    },

    {
        "name": "Potato Egg Breakfast",
        "category": "Vegetarian",
        "time": 15,
        "difficulty": "Easy",
        "emoji": "🥔",
        "ingredients": [
            "potato", "eggs", "onion", "salt"
        ],
        "instructions": [
            "Peel and cut potatoes.",
            "Cook potatoes in a pan until tender.",
            "Add chopped onion.",
            "Add beaten eggs and salt.",
            "Cook until eggs are fully set."
        ]
    }

]


# ---------------- AVAILABLE INGREDIENTS ----------------

all_ingredients = sorted(set(
    ingredient
    for recipe in recipes
    for ingredient in recipe["ingredients"]
))

# ---------------- SESSION STATE ----------------

if "my_ingredients" not in st.session_state:
    st.session_state.my_ingredients = []

if "custom_ingredients" not in st.session_state:
    st.session_state.custom_ingredients = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []


# ---------------- HEADER ----------------

st.markdown(
    '<p class="main-title">🥑 What\'s in My Fridge?</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Discover delicious recipes using ingredients you already have!</p>',
    unsafe_allow_html=True
)

st.write("")


# ---------------- SIDEBAR ----------------

st.sidebar.title("🥕 Kitchen Menu")

page = st.sidebar.radio(
    "Navigate",
    [
        "Find Recipes",
        "My Favorites",
        "About"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Your kitchen, your ingredients, your recipes! 🍅"
)


# ---------------- FIND RECIPES PAGE ----------------

if page == "Find Recipes":

    st.header("🧺 What's in your kitchen?")

    st.write(
        "Select the ingredients you currently have at home."
    )

    col1, col2 = st.columns([3, 1])

    with col1:

        selected = st.multiselect(
            "Choose your ingredients",
            options=all_ingredients,
            default=st.session_state.my_ingredients,
            placeholder="Search ingredients..."
        )

        st.session_state.my_ingredients = selected

    with col2:

        st.write("")
        st.write("")

        st.metric(
            "Selected",
            len(selected) + len(st.session_state.custom_ingredients)
        )

    # Custom ingredients

    st.subheader("➕ Add your own ingredient")

    custom_col1, custom_col2 = st.columns([3, 1])

    with custom_col1:

        new_ingredient = st.text_input(
            "Ingredient name",
            placeholder="Example: cucumber"
        )

    with custom_col2:

        st.write("")
        st.write("")

        if st.button("Add Ingredient"):

            if new_ingredient.strip():

                ingredient = new_ingredient.strip().lower()

                if ingredient not in (
                    st.session_state.my_ingredients
                    + st.session_state.custom_ingredients
                ):

                    st.session_state.custom_ingredients.append(
                        ingredient
                    )

                    st.success(f"{ingredient.title()} added!")

                    st.rerun()

                else:
                    st.warning("Ingredient already added!")

    # Display selected ingredients

    all_selected = (
        st.session_state.my_ingredients
        + st.session_state.custom_ingredients
    )

    if all_selected:

        st.write("### Your ingredients")

        st.write(", ".join(
            ingredient.title()
            for ingredient in all_selected
        ))

        if st.button("Clear All Ingredients"):

            st.session_state.my_ingredients = []
            st.session_state.custom_ingredients = []

            st.rerun()

    st.divider()

    # Recipe filters

    st.subheader("🔎 Find your perfect recipe")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:

        category = st.selectbox(
            "Recipe Type",
            [
                "All",
                "Vegetarian",
                "Non-Vegetarian"
            ]
        )

    with filter_col2:

        minimum_match = st.slider(
            "Minimum ingredient match (%)",
            min_value=0,
            max_value=100,
            value=25,
            step=5
        )

    search = st.text_input(
        "Search recipe by name",
        placeholder="Example: Pasta..."
    )

    # Find matching recipes

    if st.button("✨ Find My Recipes", use_container_width=True):

        if not all_selected:

            st.warning("Please select at least one ingredient!")

        else:

            st.session_state.search_recipes = True

    # ---------------- MATCHING LOGIC ----------------

    if (
        st.session_state.get("search_recipes", False)
        and all_selected
    ):

        matching_recipes = []

        for recipe in recipes:

            recipe_ingredients = recipe["ingredients"]

            matched = [
                ingredient
                for ingredient in recipe_ingredients
                if ingredient in all_selected
            ]

            missing = [
                ingredient
                for ingredient in recipe_ingredients
                if ingredient not in all_selected
            ]

            percentage = round(
                len(matched) / len(recipe_ingredients) * 100
            )

            # Apply filters

            if category != "All" and recipe["category"] != category:
                continue

            if percentage < minimum_match:
                continue

            if search.lower() not in recipe["name"].lower():
                continue

            matching_recipes.append({
                "recipe": recipe,
                "matched": matched,
                "missing": missing,
                "percentage": percentage
            })

        matching_recipes.sort(
            key=lambda item: item["percentage"],
            reverse=True
        )

        st.divider()

        st.header("🍽️ Recipes for you")

        st.write(
            f"We found {len(matching_recipes)} matching recipes!"
        )

        if not matching_recipes:

            st.warning(
                "No recipes found. Try selecting more ingredients "
                "or lowering your minimum match percentage."
            )

        else:

            for item in matching_recipes:

                recipe = item["recipe"]

                with st.container(border=True):

                    left, right = st.columns([1, 2])

                    with left:

                        st.markdown(
                            f"<h1 style='text-align:center;'>"
                            f"{recipe['emoji']}</h1>",
                            unsafe_allow_html=True
                        )

                        st.metric(
                            "Ingredient Match",
                            f"{item['percentage']}%"
                        )

                    with right:

                        st.subheader(recipe["name"])

                        st.caption(
                            f"⏱️ {recipe['time']} minutes  |  "
                            f"📊 {recipe['difficulty']}  |  "
                            f"🥗 {recipe['category']}"
                        )

                        st.progress(
                            item["percentage"] / 100
                        )

                        st.write("**Available ingredients:**")

                        st.write(
                            ", ".join(
                                ingredient.title()
                                for ingredient in item["matched"]
                            )
                        )

                        if item["missing"]:

                            st.write("**You still need:**")

                            st.write(
                                ", ".join(
                                    ingredient.title()
                                    for ingredient in item["missing"]
                                )
                            )

                        else:

                            st.success(
                                "You have everything needed!"
                            )

                        # Favorite button

                        if recipe["name"] in st.session_state.favorites:

                            if st.button(
                                "❤️ Remove Favorite",
                                key=f"remove_{recipe['name']}"
                            ):

                                st.session_state.favorites.remove(
                                    recipe["name"]
                                )

                                st.rerun()

                        else:

                            if st.button(
                                "🤍 Add to Favorites",
                                key=f"add_{recipe['name']}"
                            ):

                                st.session_state.favorites.append(
                                    recipe["name"]
                                )

                                st.rerun()

                    with st.expander("👩‍🍳 View Cooking Instructions"):

                        st.write("### Ingredients")

                        for ingredient in recipe["ingredients"]:

                            st.write(f"• {ingredient.title()}")

                        st.write("### Preparation Steps")

                        for number, step in enumerate(
                            recipe["instructions"], start=1
                        ):

                            st.write(f"**{number}.** {step}")


# ---------------- FAVORITES PAGE ----------------

elif page == "My Favorites":

    st.title("❤️ My Favorite Recipes")

    if not st.session_state.favorites:

        st.info(
            "You haven't saved any recipes yet. "
            "Go to Find Recipes and add your favorites!"
        )

    else:

        for recipe_name in st.session_state.favorites:

            recipe = next(
                (
                    item for item in recipes
                    if item["name"] == recipe_name
                ),
                None
            )

            if recipe:

                with st.container(border=True):

                    st.subheader(
                        f"{recipe['emoji']} {recipe['name']}"
                    )

                    st.caption(
                        f"⏱️ {recipe['time']} minutes"
                    )

                    with st.expander("View Recipe"):

                        st.write("**Ingredients**")

                        for ingredient in recipe["ingredients"]:
                            st.write(f"• {ingredient.title()}")

                        st.write("**Instructions**")

                        for step in recipe["instructions"]:
                            st.write(f"• {step}")

                    if st.button(
                        "Remove ❤️",
                        key=f"fav_remove_{recipe['name']}"
                    ):

                        st.session_state.favorites.remove(
                            recipe["name"]
                        )

                        st.rerun()


# ---------------- ABOUT PAGE ----------------

elif page == "About":

    st.title("🥑 About This Application")

    st.write("""
    What's in My Fridge? is a simple recipe discovery application.

    It helps you discover meals using ingredients already available
    in your kitchen.

    ### Features

    - Select available ingredients.
    - Add custom ingredients.
    - Discover matching recipes.
    - Calculate ingredient match percentages.
    - Find missing ingredients.
    - View cooking instructions.
    - Save your favorite recipes.

    ### Our Goal

    Reduce food waste, save money and make cooking easier!
    """)

    st.success(
        "Made with ❤️ using Python and Streamlit"
    )


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<p style='text-align:center;color:#718477;'>"
    "🥑 What's in My Fridge? | Made with Python & Streamlit"
    "</p>",
    unsafe_allow_html=True
)
