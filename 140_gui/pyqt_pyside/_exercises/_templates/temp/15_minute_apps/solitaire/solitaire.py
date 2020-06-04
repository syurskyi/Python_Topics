____ ?.QtGui ______ *
____ ?.QtWidgets ______ *
____ ?.?C.. ______ *

______ os
______ random

WINDOW_SIZE = 840, 600

CARD_DIMENSIONS = ?S..(80, 116)
CARD_RECT = QRect(0, 0, 80, 116)
CARD_SPACING_X = 110
CARD_BACK = QImage(os.pa__.join('images', 'back.png'))

DEAL_RECT = QRect(30, 30, 110, 140)

OFFSET_X = 50
OFFSET_Y = 50
WORK_STACK_Y = 200

SIDE_FACE = 0
SIDE_BACK = 1

BOUNCE_ENERGY = 0.8

# We store cards as numbers 1-13, since we only need
# to know their order for solitaire.
SUITS = ["C", "S", "H", "D"]


c_ Signals(?O..):
    complete = pS..()
    c__ = pS..()
    doubleclicked = pS..()


c_ Card(QGraphicsPixmapItem):

    ___  - (self, value, suit, $ $$
        s__(Card, self). - ($ $$)

        signals = Signals()

        stack = None  # Stack this card currently is in.
        child = None  # Card stacked on this one (for work deck).

        # Store the value & suit of the cards internal to it.
        value = value
        suit = suit
        side = None

        # For end animation only.
        vector = None

        # Cards have no internal transparent areas, so we can use this faster method.
        setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        setFlag(QGraphicsItem.ItemIsMovable)
        setFlag(QGraphicsItem.ItemSendsGeometryChanges)

        load_images()

    ___ load_images 
        face = ?P..(
            os.pa__.join('cards', '%s%s.png' % (value, suit))
        )

        back = ?P..(
            os.pa__.join('images', 'back.png')
        )

    ___ turn_face_up 
        side = SIDE_FACE
        sP..(face)

    ___ turn_back_up 
        side = SIDE_BACK
        sP..(back)

    @property
    ___ is_face_up 
        return side __ SIDE_FACE

    @property
    ___ color 
        return 'r' if suit __ ('H', 'D') ____ 'b'

    ___ mousePressEvent(self, e):
        if not is_face_up and stack.cards[-1] __ self:
            turn_face_up()  # We can do this without checking.
            e.accept()
            return

        if stack and not stack.is_free_card
            e.ignore()
            return

        stack.activate()

        e.accept()

        s__(Card, self).mouseReleaseEvent(e)

    ___ mouseReleaseEvent(self, e):
        stack.deactivate()

        i.. = collidingItems()
        if i..:
            # Find the topmost item from a different stack:
            ___ item __ i..:
                if ((isinstance(item, Card) and item.stack != stack) or
                    (isinstance(item, StackBase) and item != stack)):

                    if item.stack.is_valid_drop 
                        # Remove card + all children from previous stack, add to the new.
                        # Note: the only place there will be children is on a workstack.
                        cards = stack.remove_card
                        item.stack.add_cards(cards)
                        break

        # Refresh this card's stack, pulling it back if it was dropped.
        stack.update()

        s__(Card, self).mouseReleaseEvent(e)

    ___ mouseDoubleClickEvent(self, e):
        if stack.is_free_card
            signals.doubleclicked.e..()
            e.accept()

        s__(Card, self).mouseDoubleClickEvent(e)


c_ StackBase(QGraphicsRectItem):

    ___  - (self, $ $$
        s__(StackBase, self). - ($ $$)

        setRect(QRectF(CARD_RECT))
        setZValue(-1)

        # Cards on this deck, in order.
        cards = []

        # Store a self ref, so the collision logic can handle cards and
        # stacks with the same approach.
        stack = self
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

    ___ add_card(self, card, update= st.:
        card.stack = self
        cards.append(card)
        if update:
            update()

    ___ add_cards(self, cards):
        ___ card __ cards:
            add_card(card, update=F..)
        update()

    ___ remove_card(self, card):
        card.stack = None
        cards.remove(card)
        update()
        return [card] # Returns a list, as WorkStack must return children

    ___ remove_all_cards 
        ___ card __ cards[:]:
            card.stack = None
        cards = []

    ___ is_valid_drop(self, card):
        return T..

    ___ is_free_card(self, card):
        return F..


c_ DeckStack(StackBase):

    offset_x = -0.2
    offset_y = -0.3

    restack_counter = 0

    ___ reset 
        s__(DeckStack, self).reset()
        restack_counter = 0
        set_color(__.green)

    ___ stack_cards(self, cards):
        ___ card __ cards:
            add_card(card)
            card.turn_back_up()

    ___ can_restack(self, n_rounds=3):
        return n_rounds is None or restack_counter < n_rounds-1

    ___ update_stack_status(self, n_rounds):
        if not can_restack(n_rounds):
            set_color(__.red)
        ____:
            # We only need this if players change the round number during a game.
            set_color(__.green)

    ___ restack(self, fromstack):
        restack_counter += 1

        # We need to slice as we're adding to the list, reverse to stack back
        # in the original order.
        ___ card __ fromstack.cards[::-1]:
            fromstack.remove_card(card)
            add_card(card)
            card.turn_back_up()

    ___ take_top_card 
        ___
            card = cards[-1]
            remove_card(card)
            return card
        _____ IE..
            p..

    ___ set_color(self, color):
        color = QColor(color)
        color.setAlpha(50)
        brush = ?B..(color)
        sB..(brush)
        sP..(?P..(__.NoPen))

    ___ is_valid_drop(self, card):
        return F..


c_ DealStack(StackBase):

    offset_x = 20
    offset_y = 0

    spread_from = 0

    ___ setup 
        sP..(?P..(__.NoPen))
        color = QColor(__.black)
        color.setAlpha(50)
        brush = ?B..(color)
        sB..(brush)

    ___ reset 
        s__(DealStack, self).reset()
        spread_from = 0  # Card index to start spreading cards out.

    ___ is_valid_drop(self, card):
        return F..

    ___ is_free_card(self, card):
        return card __ cards[-1]

    ___ update 
        # Only spread the top 3 cards
        offset_x = 0
        ___ n, card __ en..(cards):
            card.setPos(pos() + QPointF(offset_x, 0))
            card.setZValue(n)

            if n >= spread_from:
                offset_x = offset_x + offset_x


c_ WorkStack(StackBase):

    offset_x = 0
    offset_y = 15
    offset_y_back = 5

    ___ setup 
        sP..(?P..(__.NoPen))
        color = QColor(__.black)
        color.setAlpha(50)
        brush = ?B..(color)
        sB..(brush)

    ___ activate 
        # Raise z-value of this stack so children float above all other cards.
        setZValue(1000)

    ___ deactivate 
        setZValue(-1)

    ___ is_valid_drop(self, card):
        if not cards:
            return T..

        if (card.color != cards[-1].color and
            card.value __ cards[-1].value -1):
            return T..

        return F..

    ___ is_free_card(self, card):
        return card.is_face_up #self.cards and card == self.cards[-1]

    ___ add_card(self, card, update= st.:
        if cards:
            card.setParentItem(cards[-1])
        ____:
            card.setParentItem

        s__(WorkStack, self).add_card(card, update=update)

    ___ remove_card(self, card):
        index = cards.index(card)
        cards, cards = cards[:index], cards[index:]

        ___ card __ cards:
            # Remove card and all children, returning a list of cards removed in order.
            card.setParentItem(None)
            card.stack = None

        update()
        return cards

    ___ remove_all_cards 
        ___ card __ cards[:]:
            card.setParentItem(None)
            card.stack = None
        cards = []

    ___ update 
        stack.setZValue(-1) # Reset this stack the the background.
        # Only spread the top 3 cards
        offset_y = 0
        ___ n, card __ en..(cards):
            card.setPos(QPointF(0, offset_y))

            if card.is_face_up:
                offset_y = offset_y
            ____:
                offset_y = offset_y_back


c_ DropStack(StackBase):

    offset_x = -0.2
    offset_y = -0.3

    suit = None
    value = 0

    ___ setup 
        signals = Signals()
        color = QColor(__.blue)
        color.setAlpha(50)
        pen = ?P..(color)
        pen.sW..(5)
        sP..(pen)

    ___ reset 
        s__(DropStack, self).reset()
        suit = None
        value = 0

    ___ is_valid_drop(self, card):
        if ((suit is None or card.suit __ suit) and
                (card.value __ value + 1)):
            return T..

        return F..

    ___ add_card(self, card, update= st.:
        s__(DropStack, self).add_card(card, update=update)
        suit = card.suit
        value = cards[-1].value

        if is_complete:
            signals.complete.e..()

    ___ remove_card(self, card):
        s__(DropStack, self).remove_card(card)
        value = cards[-1].value if cards ____ 0

    @property
    ___ is_complete 
        return value __ 13


c_ DealTrigger(QGraphicsRectItem):

    ___  - (self, $ $$
        s__(DealTrigger, self). - ($ $$)
        setRect(QRectF(DEAL_RECT))
        setZValue(1000)

        pen = ?P..(__.NoPen)
        sP..(pen)

        signals = Signals()

    ___ mousePressEvent(self, e):
        signals.c__.e..()


c_ AnimationCover(QGraphicsRectItem):
    ___  - (self, $ $$
        s__(AnimationCover, self). - ($ $$)
        setRect(QRectF(0, 0, *WINDOW_SIZE))
        setZValue(5000)
        pen = ?P..(__.NoPen)
        sP..(pen)

    ___ mousePressEvent(self, e):
        e.accept()


c_ MainWindow(?MW..):

    ___  - (self, $ $$
        s__(MainWindow, self). - ($ $$)

        view = QGraphicsView()
        scene = QGraphicsScene()
        scene.setSceneRect(QRectF(0, 0, *WINDOW_SIZE))

        felt = ?B..(?P..(os.pa__.join('images','felt.png')))
        scene.setBackgroundBrush(felt)

        name = QGraphicsPixmapItem()
        name.sP..(?P..(os.pa__.join('images','ronery.png')))
        name.setPos(QPointF(170, 375))
        scene.aI..(name)

        view.setScene(scene)

        # Timer for the win animation only.
        timer = ?T..()
        timer.sI..(5)
        timer.timeout.c__(win_animation)

        animation_event_cover = AnimationCover()
        scene.aI..(animation_event_cover)

        menu = menuBar().addMenu("&Game")

        deal_action = ?A..(?I..(os.pa__.join('images', 'playing-card.png')), "Deal...", self)
        deal_action.t___.c__(restart_game)
        menu.aA..(deal_action)

        menu.addSeparator()

        deal1_action = ?A..("1 card", self)
        deal1_action.setCheckable( st.
        deal1_action.t___.c__(l___: set_deal_n(1))
        menu.aA..(deal1_action)

        deal3_action = ?A..("3 card", self)
        deal3_action.setCheckable( st.
        deal3_action.sC__( st.
        deal3_action.t___.c__(l___: set_deal_n(3))

        menu.aA..(deal3_action)

        dealgroup = QActionGroup
        dealgroup.aA..(deal1_action)
        dealgroup.aA..(deal3_action)
        dealgroup.setExclusive( st.

        menu.addSeparator()

        rounds3_action = ?A..("3 rounds", self)
        rounds3_action.setCheckable( st.
        rounds3_action.sC__( st.
        rounds3_action.t___.c__(l___: set_rounds_n(3))
        menu.aA..(rounds3_action)

        rounds5_action = ?A..("5 rounds", self)
        rounds5_action.setCheckable( st.
        rounds5_action.t___.c__(l___: set_rounds_n(5))
        menu.aA..(rounds5_action)

        roundsu_action = ?A..("Unlimited rounds", self)
        roundsu_action.setCheckable( st.
        roundsu_action.t___.c__(l___: set_rounds_n(None))
        menu.aA..(roundsu_action)

        roundgroup = QActionGroup
        roundgroup.aA..(rounds3_action)
        roundgroup.aA..(rounds5_action)
        roundgroup.aA..(roundsu_action)
        roundgroup.setExclusive( st.

        menu.addSeparator()

        quit_action = ?A..("Quit", self)
        quit_action.t___.c__(quit)
        menu.aA..(quit_action)

        deck = []
        deal_n = 3  # Number of cards to deal each time
        rounds_n = 3  # Number of rounds (restacks) before end.

        ___ suit __ SUITS:
            ___ value __ ra..(1, 14):
                card = Card(value, suit)
                deck.append(card)
                scene.aI..(card)
                card.signals.doubleclicked.c__(l___ card=card: auto_drop_card(card))

        setCentralWidget(view)
        sFS..(*WINDOW_SIZE)

        deckstack = DeckStack()
        deckstack.setPos(OFFSET_X, OFFSET_Y)
        scene.aI..(deckstack)

        # Set up the working locations.
        works = []
        ___ n __ ra..(7):
            stack = WorkStack()
            stack.setPos(OFFSET_X + CARD_SPACING_X*n, WORK_STACK_Y)
            scene.aI..(stack)
            works.append(stack)

        drops = []
        # Set up the drop locations.
        ___ n __ ra..(4):
            stack = DropStack()
            stack.setPos(OFFSET_X + CARD_SPACING_X * (3+n), OFFSET_Y)
            stack.signals.complete.c__(check_win_condition)

            scene.aI..(stack)
            drops.append(stack)

        # Add the deal location.
        dealstack = DealStack()
        dealstack.setPos(OFFSET_X + CARD_SPACING_X, OFFSET_Y)
        scene.aI..(dealstack)

        # Add the deal click-trigger.
        dealtrigger = DealTrigger()
        dealtrigger.signals.c__.c__(deal)
        scene.aI..(dealtrigger)

        shuffle_and_stack()

        sWT..("Ronery")
        s..

    ___ restart_game 
        reply = QMessageBox.question(self, "Deal again", "Are you sure you want to start a new game?",
                                      QMessageBox.Yes | QMessageBox.No)

        if reply __ QMessageBox.Yes:
            shuffle_and_stack()

    ___ quit 
        c..

    ___ set_deal_n(self, n):
        deal_n = n

    ___ set_rounds_n(self, n):
        rounds_n = n
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
        cards = deck[:]
        ___ n, workstack __ en..(works, 1):
            ___ a __ ra..(n):
                card = cards.pop()
                workstack.add_card(card)
                card.turn_back_up()
                if a __ n-1:
                    card.turn_face_up()

        # Ensure removed from all other stacks here.
        deckstack.stack_cards(cards)

    ___ deal 
        if deckstack.cards:
            dealstack.spread_from = len(dealstack.cards)
            ___ n __ ra..(deal_n):
                card = deckstack.take_top_card()
                if card:
                    dealstack.add_card(card)
                    card.turn_face_up()

        elif deckstack.can_restack(rounds_n):
            deckstack.restack(dealstack)
            deckstack.update_stack_status(rounds_n)

    ___ auto_drop_card(self, card):
        ___ stack __ drops:
            if stack.is_valid_drop(card):
                card.stack.remove_card(card)
                stack.add_card(card)
                break

    ___ check_win_condition 
        complete = al.(s.is_complete ___ s __ drops)
        if complete:
            # Add click-proof cover to play area.
            animation_event_cover.s..
            # Get the stacks of cards from the drop,stacks.
            timer.start()

    ___ win_animation 
        # Start off a new card
        ___ drop __ drops:
            if drop.cards:
                card = drop.cards.pop()
                if card.vector is None:
                    card.vector = QPoint(-random.randint(3, 10), -random.randint(0, 10))
                    break

        ___ card __ deck:
            if card.vector is not None:
                card.setPos(card.pos() + card.vector)
                card.vector += QPoint(0, 1)  # Gravity
                if card.pos().y() > WINDOW_SIZE[1] - CARD_DIMENSIONS.height():
                    # Bounce the card, losing some energy.
                    card.vector = QPoint(card.vector.x(), -max(1, int(card.vector.y() * BOUNCE_ENERGY)) )
                    # Bump back up to base of screen.
                    card.setPos(card.pos().x(), WINDOW_SIZE[1] - CARD_DIMENSIONS.height())

                if card.pos().x() < - CARD_DIMENSIONS.width():
                    card.vector = None
                    # Put the card back where it started.
                    card.stack.add_card(card)





if __name__ __ '__main__':

    app = ?A..([])
    window = MainWindow()
    app.e..()