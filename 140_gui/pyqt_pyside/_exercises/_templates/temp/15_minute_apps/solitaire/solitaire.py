____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

______ __
______ random

WINDOW_SIZE _ 840, 600

CARD_DIMENSIONS _ ?S..(80, 116)
CARD_RECT _ QRect(0, 0, 80, 116)
CARD_SPACING_X _ 110
CARD_BACK _ QImage(__.pa__.join('images', 'back.png'))

DEAL_RECT _ QRect(30, 30, 110, 140)

OFFSET_X _ 50
OFFSET_Y _ 50
WORK_STACK_Y _ 200

SIDE_FACE _ 0
SIDE_BACK _ 1

BOUNCE_ENERGY _ 0.8

# We store cards as numbers 1-13, since we only need
# to know their order for solitaire.
SUITS _ ["C", "S", "H", "D"]


c_ Signals(?O..):
    complete _ pS..()
    c__ _ pS..()
    doubleclicked _ pS..()


c_ Card(QGraphicsPixmapItem):

    ___  -   value, suit, $ $$
        s__(Card, self). - ($ $$)

        signals _ Signals()

        stack _ None  # Stack this card currently is in.
        child _ None  # Card stacked on this one (for work deck).

        # Store the value & suit of the cards internal to it.
        value _ value
        suit _ suit
        side _ None

        # For end animation only.
        vector _ None

        # Cards have no internal transparent areas, so we can use this faster method.
        setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        setFlag(QGraphicsItem.ItemIsMovable)
        setFlag(QGraphicsItem.ItemSendsGeometryChanges)

        load_images()

    ___ load_images 
        face _ ?P..(
            __.pa__.join('cards', '%s%s.png' % (value, suit))
        )

        back _ ?P..(
            __.pa__.join('images', 'back.png')
        )

    ___ turn_face_up 
        side _ SIDE_FACE
        sP..(face)

    ___ turn_back_up 
        side _ SIDE_BACK
        sP..(back)

    @property
    ___ is_face_up 
        r_ side __ SIDE_FACE

    @property
    ___ color 
        r_ 'r' __ suit __ ('H', 'D') ____ 'b'

    ___ mousePressEvent  e):
        __ not is_face_up and stack.cards[-1] __ self:
            turn_face_up()  # We can do this without checking.
            e.accept()
            r_

        __ stack and not stack.is_free_card
            e.ignore()
            r_

        stack.activate()

        e.accept()

        s__(Card, self).mouseReleaseEvent(e)

    ___ mouseReleaseEvent  e):
        stack.deactivate()

        i.. _ collidingItems()
        __ i..:
            # Find the topmost item from a different stack:
            ___ item __ i..:
                __ ((isinstance(item, Card) and item.stack !_ stack) or
                    (isinstance(item, StackBase) and item !_ stack)):

                    __ item.stack.is_valid_drop 
                        # Remove card + all children from previous stack, add to the new.
                        # Note: the only place there will be children is on a workstack.
                        cards _ stack.remove_card
                        item.stack.add_cards(cards)
                        break

        # Refresh this card's stack, pulling it back if it was dropped.
        stack.update()

        s__(Card, self).mouseReleaseEvent(e)

    ___ mouseDoubleClickEvent  e):
        __ stack.is_free_card
            signals.doubleclicked.e..()
            e.accept()

        s__(Card, self).mouseDoubleClickEvent(e)


c_ StackBase(QGraphicsRectItem):

    ___  -   $ $$
        s__(StackBase, self). - ($ $$)

        setRect(QRectF(CARD_RECT))
        setZValue(-1)

        # Cards on this deck, in order.
        cards _   # list

        # Store a self ref, so the collision logic can handle cards and
        # stacks with the same approach.
        stack _ self
        setup()
        reset()

    ___ setup 
        p..

    ___ reset 
        remove_all_cards()

    ___ update 
        ___ n, card __ en..(cards):
            card.setPos( pos() + QPointF(n * offset_x, n * offset_y))
            card.setZValue(n)

    ___ activate 
        p..

    ___ deactivate 
        p..

    ___ add_card  card, update_ st.:
        card.stack _ self
        cards.ap..(card)
        __ update:
            update()

    ___ add_cards  cards):
        ___ card __ cards:
            add_card(card, update_F..)
        update()

    ___ remove_card  card):
        card.stack _ None
        cards.remove(card)
        update()
        r_ [card] # Returns a list, as WorkStack must return children

    ___ remove_all_cards 
        ___ card __ cards[:]:
            card.stack _ None
        cards _   # list

    ___ is_valid_drop  card):
        r_ T..

    ___ is_free_card  card):
        r_ F..


c_ DeckStack(StackBase):

    offset_x _ -0.2
    offset_y _ -0.3

    restack_counter _ 0

    ___ reset 
        s__(DeckStack, self).reset()
        restack_counter _ 0
        set_color(__.green)

    ___ stack_cards  cards):
        ___ card __ cards:
            add_card(card)
            card.turn_back_up()

    ___ can_restack  n_rounds_3):
        r_ n_rounds is None or restack_counter < n_rounds-1

    ___ update_stack_status  n_rounds):
        __ not can_restack(n_rounds):
            set_color(__.red)
        ____:
            # We only need this if players change the round number during a game.
            set_color(__.green)

    ___ restack  fromstack):
        restack_counter +_ 1

        # We need to slice as we're adding to the list, reverse to stack back
        # in the original order.
        ___ card __ fromstack.cards[::-1]:
            fromstack.remove_card(card)
            add_card(card)
            card.turn_back_up()

    ___ take_top_card 
        ___
            card _ cards[-1]
            remove_card(card)
            r_ card
        _____ IE..
            p..

    ___ set_color  color):
        color _ QColor(color)
        color.setAlpha(50)
        brush _ ?B..(color)
        sB..(brush)
        sP..(?P..(__.NoPen))

    ___ is_valid_drop  card):
        r_ F..


c_ DealStack(StackBase):

    offset_x _ 20
    offset_y _ 0

    spread_from _ 0

    ___ setup 
        sP..(?P..(__.NoPen))
        color _ QColor(__.black)
        color.setAlpha(50)
        brush _ ?B..(color)
        sB..(brush)

    ___ reset 
        s__(DealStack, self).reset()
        spread_from _ 0  # Card index to start spreading cards out.

    ___ is_valid_drop  card):
        r_ F..

    ___ is_free_card  card):
        r_ card __ cards[-1]

    ___ update 
        # Only spread the top 3 cards
        offset_x _ 0
        ___ n, card __ en..(cards):
            card.setPos(pos() + QPointF(offset_x, 0))
            card.setZValue(n)

            __ n >_ spread_from:
                offset_x _ offset_x + offset_x


c_ WorkStack(StackBase):

    offset_x _ 0
    offset_y _ 15
    offset_y_back _ 5

    ___ setup 
        sP..(?P..(__.NoPen))
        color _ QColor(__.black)
        color.setAlpha(50)
        brush _ ?B..(color)
        sB..(brush)

    ___ activate 
        # Raise z-value of this stack so children float above all other cards.
        setZValue(1000)

    ___ deactivate 
        setZValue(-1)

    ___ is_valid_drop  card):
        __ not cards:
            r_ T..

        __ (card.color !_ cards[-1].color and
            card.value __ cards[-1].value -1):
            r_ T..

        r_ F..

    ___ is_free_card  card):
        r_ card.is_face_up #self.cards and card == self.cards[-1]

    ___ add_card  card, update_ st.:
        __ cards:
            card.setParentItem(cards[-1])
        ____:
            card.setParentItem

        s__(WorkStack, self).add_card(card, update_update)

    ___ remove_card  card):
        index _ cards.index(card)
        cards, cards _ cards[:index], cards[index:]

        ___ card __ cards:
            # Remove card and all children, returning a list of cards removed in order.
            card.setParentItem(None)
            card.stack _ None

        update()
        r_ cards

    ___ remove_all_cards 
        ___ card __ cards[:]:
            card.setParentItem(None)
            card.stack _ None
        cards _   # list

    ___ update 
        stack.setZValue(-1) # Reset this stack the the background.
        # Only spread the top 3 cards
        offset_y _ 0
        ___ n, card __ en..(cards):
            card.setPos(QPointF(0, offset_y))

            __ card.is_face_up:
                offset_y _ offset_y
            ____:
                offset_y _ offset_y_back


c_ DropStack(StackBase):

    offset_x _ -0.2
    offset_y _ -0.3

    suit _ None
    value _ 0

    ___ setup 
        signals _ Signals()
        color _ QColor(__.blue)
        color.setAlpha(50)
        pen _ ?P..(color)
        pen.sW..(5)
        sP..(pen)

    ___ reset 
        s__(DropStack, self).reset()
        suit _ None
        value _ 0

    ___ is_valid_drop  card):
        __ ((suit is None or card.suit __ suit) and
                (card.value __ value + 1)):
            r_ T..

        r_ F..

    ___ add_card  card, update_ st.:
        s__(DropStack, self).add_card(card, update_update)
        suit _ card.suit
        value _ cards[-1].value

        __ is_complete:
            signals.complete.e..()

    ___ remove_card  card):
        s__(DropStack, self).remove_card(card)
        value _ cards[-1].value __ cards ____ 0

    @property
    ___ is_complete 
        r_ value __ 13


c_ DealTrigger(QGraphicsRectItem):

    ___  -   $ $$
        s__(DealTrigger, self). - ($ $$)
        setRect(QRectF(DEAL_RECT))
        setZValue(1000)

        pen _ ?P..(__.NoPen)
        sP..(pen)

        signals _ Signals()

    ___ mousePressEvent  e):
        signals.c__.e..()


c_ AnimationCover(QGraphicsRectItem):
    ___  -   $ $$
        s__(AnimationCover, self). - ($ $$)
        setRect(QRectF(0, 0, *WINDOW_SIZE))
        setZValue(5000)
        pen _ ?P..(__.NoPen)
        sP..(pen)

    ___ mousePressEvent  e):
        e.accept()


c_ MainWindow(?MW..):

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)

        view _ QGraphicsView()
        scene _ QGraphicsScene()
        scene.setSceneRect(QRectF(0, 0, *WINDOW_SIZE))

        felt _ ?B..(?P..(__.pa__.join('images','felt.png')))
        scene.setBackgroundBrush(felt)

        name _ QGraphicsPixmapItem()
        name.sP..(?P..(__.pa__.join('images','ronery.png')))
        name.setPos(QPointF(170, 375))
        scene.aI..(name)

        view.setScene(scene)

        # Timer for the win animation only.
        timer _ ?T..()
        timer.sI..(5)
        timer.timeout.c__(win_animation)

        animation_event_cover _ AnimationCover()
        scene.aI..(animation_event_cover)

        menu _ mB...aM..("&Game")

        deal_action _ ?A..(?I..(__.pa__.join('images', 'playing-card.png')), "Deal...", self)
        deal_action.t___.c__(restart_game)
        menu.aA..(deal_action)

        menu.aS..)

        deal1_action _ ?A..("1 card", self)
        deal1_action.setCheckable( st.
        deal1_action.t___.c__(l___: set_deal_n(1))
        menu.aA..(deal1_action)

        deal3_action _ ?A..("3 card", self)
        deal3_action.setCheckable( st.
        deal3_action.sC__( st.
        deal3_action.t___.c__(l___: set_deal_n(3))

        menu.aA..(deal3_action)

        dealgroup _ QActionGroup
        dealgroup.aA..(deal1_action)
        dealgroup.aA..(deal3_action)
        dealgroup.setExclusive( st.

        menu.aS..)

        rounds3_action _ ?A..("3 rounds", self)
        rounds3_action.setCheckable( st.
        rounds3_action.sC__( st.
        rounds3_action.t___.c__(l___: set_rounds_n(3))
        menu.aA..(rounds3_action)

        rounds5_action _ ?A..("5 rounds", self)
        rounds5_action.setCheckable( st.
        rounds5_action.t___.c__(l___: set_rounds_n(5))
        menu.aA..(rounds5_action)

        roundsu_action _ ?A..("Unlimited rounds", self)
        roundsu_action.setCheckable( st.
        roundsu_action.t___.c__(l___: set_rounds_n(None))
        menu.aA..(roundsu_action)

        roundgroup _ QActionGroup
        roundgroup.aA..(rounds3_action)
        roundgroup.aA..(rounds5_action)
        roundgroup.aA..(roundsu_action)
        roundgroup.setExclusive( st.

        menu.aS..)

        quit_action _ ?A..("Quit", self)
        quit_action.t___.c__(quit)
        menu.aA..(quit_action)

        deck _   # list
        deal_n _ 3  # Number of cards to deal each time
        rounds_n _ 3  # Number of rounds (restacks) before end.

        ___ suit __ SUITS:
            ___ value __ ra..(1, 14):
                card _ Card(value, suit)
                deck.ap..(card)
                scene.aI..(card)
                card.signals.doubleclicked.c__(l___ card_card: auto_drop_card(card))

        setCentralWidget(view)
        sFS..(*WINDOW_SIZE)

        deckstack _ DeckStack()
        deckstack.setPos(OFFSET_X, OFFSET_Y)
        scene.aI..(deckstack)

        # Set up the working locations.
        works _   # list
        ___ n __ ra..(7):
            stack _ WorkStack()
            stack.setPos(OFFSET_X + CARD_SPACING_X*n, WORK_STACK_Y)
            scene.aI..(stack)
            works.ap..(stack)

        drops _   # list
        # Set up the drop locations.
        ___ n __ ra..(4):
            stack _ DropStack()
            stack.setPos(OFFSET_X + CARD_SPACING_X * (3+n), OFFSET_Y)
            stack.signals.complete.c__(check_win_condition)

            scene.aI..(stack)
            drops.ap..(stack)

        # Add the deal location.
        dealstack _ DealStack()
        dealstack.setPos(OFFSET_X + CARD_SPACING_X, OFFSET_Y)
        scene.aI..(dealstack)

        # Add the deal click-trigger.
        dealtrigger _ DealTrigger()
        dealtrigger.signals.c__.c__(deal)
        scene.aI..(dealtrigger)

        shuffle_and_stack()

        sWT..("Ronery")
        s..

    ___ restart_game 
        reply _ ?MB...question  "Deal again", "Are you sure you want to start a new game?",
                                      ?MB...Yes | ?MB...No)

        __ reply __ ?MB...Yes:
            shuffle_and_stack()

    ___ quit 
        c..

    ___ set_deal_n  n):
        deal_n _ n

    ___ set_rounds_n  n):
        rounds_n _ n
        deckstack.update_stack_status(rounds_n)

    ___ shuffle_and_stack 
        # Stop any ongoing animation.
        timer.s..
        animation_event_cover.hide()

        # Remove cards from all stacks.
        ___ stack __ [deckstack, dealstack] + drops + works:
            stack.reset()

        random.shuffle(deck)

        # Deal out from the top of the deck, turning over the
        # final card on each line.
        cards _ deck[:]
        ___ n, workstack __ en..(works, 1):
            ___ a __ ra..(n):
                card _ cards.pop()
                workstack.add_card(card)
                card.turn_back_up()
                __ a __ n-1:
                    card.turn_face_up()

        # Ensure removed from all other stacks here.
        deckstack.stack_cards(cards)

    ___ deal 
        __ deckstack.cards:
            dealstack.spread_from _ le.(dealstack.cards)
            ___ n __ ra..(deal_n):
                card _ deckstack.take_top_card()
                __ card:
                    dealstack.add_card(card)
                    card.turn_face_up()

        elif deckstack.can_restack(rounds_n):
            deckstack.restack(dealstack)
            deckstack.update_stack_status(rounds_n)

    ___ auto_drop_card  card):
        ___ stack __ drops:
            __ stack.is_valid_drop(card):
                card.stack.remove_card(card)
                stack.add_card(card)
                break

    ___ check_win_condition 
        complete _ al.(s.is_complete ___ s __ drops)
        __ complete:
            # Add click-proof cover to play area.
            animation_event_cover.s..
            # Get the stacks of cards from the drop,stacks.
            timer.start()

    ___ win_animation 
        # Start off a new card
        ___ drop __ drops:
            __ drop.cards:
                card _ drop.cards.pop()
                __ card.vector is N..
                    card.vector _ QPoint(-random.randint(3, 10), -random.randint(0, 10))
                    break

        ___ card __ deck:
            __ card.vector is not N..
                card.setPos(card.pos() + card.vector)
                card.vector +_ QPoint(0, 1)  # Gravity
                __ card.pos().y() > WINDOW_SIZE[1] - CARD_DIMENSIONS.height():
                    # Bounce the card, losing some energy.
                    card.vector _ QPoint(card.vector.x(), -max(1, in.(card.vector.y() * BOUNCE_ENERGY)) )
                    # Bump back up to base of screen.
                    card.setPos(card.pos().x(), WINDOW_SIZE[1] - CARD_DIMENSIONS.height())

                __ card.pos().x() < - CARD_DIMENSIONS.width():
                    card.vector _ None
                    # Put the card back where it started.
                    card.stack.add_card(card)





__ __name__ __ '__main__':

    app _ ?A..([])
    window _ MainWindow()
    app.e..()