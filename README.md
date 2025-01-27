**26/01/25**

    - Made a massive breakthrough in multiple fronts.
    - Finally got the `Stack` class working.
        - Every card will be in a `Stack` list.
        - The `Stack` list has access to the `Card` class letting it set `parent` and `childrens`
        - This also allowed me to render `stack` lists instead of card objects.
    - Figured out py`game does not differentiate two objects if they overlap.
    - Reading `stack` lists in reverse I was able to overcome pygame limitations.

**25/01/25:**

    - Was forced to start looking in to game loop.
    - Figured out how to add drag and drop.
    - Figured out an approach for handling card stacking.
        - Looked at some code on how Solitaire does card stacking.
        - Learned of defining `parent` and `child` in the `Card` class.
        - Copied the `Stack` class and now trying to uderstand how this code works.
        - `Stack` class manages cards. It checks and sets the parent for the Card class.
        - `Stack` class handles adding, removing and creating new stacks of cards.
    - Added `stack.py`.
    - main game loop looks very messy atm.

**24/01/25:**

    - Broke the project into different files `main.py`, `card.py`, `ability.py` and `render.py`.
    - Have a plan for my approach now:
        - `Card` class will cover every card.
        - `WitchCard` class  part of `card.py `will cover every controlable unit.
        - `Ability` class will detail all actions any card can perform.
        - `Render` class and file will separate the game logic from the game rendering.
        - `Main` file to focus on game loop.
    - After fighting with chatGPT figured out how to handle abilities.
        - Every ability will be a subclass of `Abilities` class.
        - Will hold the `action` and `trigger`
        - Every card type that can performe an action will have a predefined list of `_abilities`.
    - Have to figure out how to do Summoning/Crafting.

**23/01/25:**

    - Finally starting to understand OOP better and started to get an idea of how to design my code.
    - Spoke to Babbit about my approach.
    - Due to frustration I decided to look into `PyGame`. Wrote my first custome `draw_card()` method.
    - Woo hoo first ever actual use for `tuples` to define colour.

**19/01/25:**

    - Deleted everything and only kept the base `Card` class.
    - Spent more time doing trial and error with my approach.

**17/01/25:**

    - Messed around with trying to figure out different types of cards.
    - Created a lot of subclasses.

**15/01/25:**

    - Decided to try and learn more about OOP by trying to create a game where everything is represented as cards.
    - Managed with the help of chatGPT to create the base `Card` class.