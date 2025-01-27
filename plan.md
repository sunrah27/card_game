# Building core game logic

## Step 1: Overlap Detection for Stacking
    1. Center-Based Method:
        * We’ll calculate the center of the dragged card and check how much it overlaps with the centers of other cards.
        * The card with the highest overlap percentage will be the target for stacking.
        * If the dragged card does not sufficiently overlap with any other card, it will return to its original position.
        * We'll use an overlap percentage-based threshold for stacking. For example, at least 50% of the dragged card's center must overlap the target card's space to stack.
        * We'll make this value configurable for future testing.

    2. Behavior When Overlap Is Detected:
        * Once a valid overlap is detected:
            * Verify if the stacking conditions are met (e.g., WitchCard can stack on EnemyCard, or WitchCard can stack on another WitchCard).
            * Adjust the x and y positions of the dragged card based on the stack (maintaining offsets for proper visuals).

    3. Edge Cases:
        * Ensure overlapping two cards that are close to each other works without ambiguity.
        * Handle situations where multiple stacks are near each other.

**Step 2: Drag-and-Drop Mechanics**
    1. Dragging Player-Controlled Cards:
        * Only WitchCard-class cards (Witch, Warrior, Mage) are draggable.
        * While dragging:
            * Highlight the card being dragged.
            * Temporarily remove it from its stack visually but keep its stack data intact.

    2. Dropping the Card:
        * After release, check:
            * If the card overlaps another card and can stack, place it in the correct position in the stack.
            * If it cannot stack, return it to its original position.

    3. Interaction with the Arena:
        * Ensure cards cannot overlap with other cards unless stacking is possible.
        * Cards must stay within the arena boundaries.

**Step 3: Stacking Mechanics**
    1. Stack Structure:
        * Internal Representation: Maintain each stack as a list, where index 0 is the bottom card, and the last index is the top card.
            * Example: `[EnemyCard, WitchCard, WarriorCard]`
        * Each card knows its stack position and its parent stack (if any).

    2. Behavior for Stacks:
        * Top Card Actions: Only the top-most card in the stack can perform actions (attack, explore, etc.).
        * Death of Top Card:
            * If the top card dies, the next card in the stack automatically becomes active.
            * Death animation and the next card’s attack (if applicable) occur simultaneously.
        * Enemy Card Removal:
            * If an EnemyCard at the bottom of the stack is destroyed, the stack above it remains in the same position.
            * Example: `[EnemyCard, WitchCard, WarriorCard]` → `[WitchCard, WarriorCard]`.

    3. Splitting a Stack:
        * Players can split a stack by dragging any visible part of a card within the stack:
            * For example: In a stack [Card1, Card2, Card3, Card4], dragging Card2 will create two stacks:
                * `[Card1]` stays in its position.
                * `[Card2, Card3, Card4]` becomes a new stack.
        * Adjust the visual positions of both stacks accordingly.
        * Stacks can always be split by dragging any visible card.
            * If the top card of a stack is in the process of performing an action (e.g., attack), removing the card will reset the action timer for that specific action.
            * This adds an element of strategy and risk: splitting stacks mid-action can disrupt progress.
        * Splitting a stack will create two separate stacks:
            * The dragged card and all cards above it will form a new stack.
            * The remaining cards stay as the original stack.

**Step 4: Stacking Logic for the Future**
    1. Stack Requirements for Recipes:
        * For future mechanics, stacks may need to meet specific conditions to perform actions like crafting, summoning, or casting spells.
        * Conditions can involve:
            * Specific card types (e.g., “WitchCard + ResourceCard”).
            * Specific stack orders (e.g., “CardA must be above CardB”).
            * Stack sizes (e.g., “Stack must contain at least 3 cards”).

    2. Spell Blueprint – Healing Touch:
        * Required: Healing Touch Blueprint, Reagent, Mana, and a Witch card with the ability to cast spells.
        * Logic:
            * Verify the stack contains all required card types.
            * The specific order of cards in the stack does not matter.
            * When the spell is cast (e.g., after 10 seconds), the following happens:
                * Reagent and Mana cards are consumed.
                * Blueprint and Witch cards remain in the stack.

    3. Building Blueprint – Arcane School:
        * Required: Arcane School Blueprint, Crystal x3, Stardrop x1, and a Witch.
        * Logic:
            * Verify the stack contains the required card types in the specified quantities.
            * On completion, Blueprint and Witch cards remain, while the rest are consumed.

    4. Flexibility:
        * This logic ensures recipes can vary by:
            * Required card types.
            * Specific quantities (e.g., Crystal x3).
            * Cards that remain vs. those that are consumed.

**Step 5: Integration into Game Loop**
    1. Time-Based Actions:
        * Add timing mechanics to prevent rapid actions (e.g., 10-second charge time for attacks).
        * During an attack:
            * The WitchCard remains locked in the stack.
            * Once the attack completes, apply damage to both the WitchCard and the EnemyCard.

    2. Stack Management During Game Cycle:
        * Allow dynamic stack creation, splitting, and destruction as the player interacts with cards during their turn.
        * Maintain stack consistency during transitions (e.g., when the day ends or new cards are added to the arena).

    3. Witching Hour:
        * At the end of the 180-second day cycle:
            * Damage the singleton WitchCard by 1 * number of EnemyCards on the arena.
        * Ensure this mechanic accounts for all stacks and does not interfere with player actions.
        * During the witching hour:
            * The player loses control of the game.
            * The singleton Witch card takes 1 damage per EnemyCard on the arena.
            * Future visualizations could include:
                * A darkened screen.
                * Visual effects for the damage taken by the Witch.

    4. Post-witching hour:
        * The next day starts (e.g., Day 2).
        * The player regains control.

**6. Rendering and Interaction**
    1. Rendering Stacked Cards:
        * Stacked cards will be visually offset by 42 pixels on the Y-axis.
        * Example:
            * If the bottom card is at (x=123, y=563), the second card will render at (x=123, y=605), the third at (x=123, y=647), and so on.
            * This ensures the player can clearly see all cards in the stack.

    2. Interaction:
        * When hovering or dragging cards, highlight the selected card or stack for better visibility.
        * Ensure cards snap to valid stack positions or return to their original position if stacking is invalid.