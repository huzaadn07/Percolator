import pygame

# default card specs
CARD_WIDTH = 70
CARD_HEIGHT = 105
CARD_SPACING = 12
HAND_Y_BASE = 230
# default colours picked
CARD_BG_COLOUR = (245, 238, 220)
CARD_BORDER_COLOUR = (60, 45, 35)
HOVER_BORDER_COLOUR = (215, 150, 40)
HEADER_BG_COLOUR = (195, 160, 120)
TEXT_COLOUR = (45, 35, 30)

class CardUI:
    def __init__(self, name, cardType, basePoints): # parameters taken from entities.py
        self.name = name
        self.cardType = cardType
        self.basePoints = basePoints

        self.rect = pygame.Rect(0, 0, CARD_WIDTH, CARD_HEIGHT)
        self.isHovered = False
        self.isSelected = False
        
    def draw(self, surface, font, smallFont):
        hoverOffset = 0 
        if (self.isHovered or self.isSelected): # lift card by 12 pixels
            hoverOffset = 12
        renderRect = pygame.Rect(
            self.rect.x,
            self.rect.y - hoverOffset, # lift card if hovering/selected
            self.rect.width,
            self.rect.height
        )

        # card design interaction
        borderColour = CARD_BORDER_COLOUR
        if self.isHovered:
            borderColour = HOVER_BORDER_COLOUR
        innerRect = renderRect.inflate(-4, -4)
        headerRect = pygame.Rect(innerRect.x, innerRect.y, innerRect.width, 24)
        titleSurface = smallFont.render(self.name, True, TEXT_COLOUR)
        pointsSurface = font.render(str(self.basePoints), True, TEXT_COLOUR)
        titleX = headerRect.x + (headerRect.width - titleSurface.get_width()) // 2 # position title of card
        pointsX = innerRect.x + (innerRect.width - pointsSurface.get_width()) // 2 # position points of card

        # drawing these features
        pygame.draw.rect(surface, borderColour, renderRect, border_radius=6)
        pygame.draw.rect(surface, CARD_BG_COLOUR, innerRect, border_radius=4)
        pygame.draw.rect(surface, HEADER_BG_COLOUR, headerRect, border_top_left_radius=4, border_top_right_radius=4)
        pointsSurface = font.render(str(self.basePoints), True, TEXT_COLOUR)
        surface.blit(titleSurface, (titleX, headerRect.y + 5))
        surface.blit(pointsSurface, (pointsX, innerRect.y + 45))

class UIManager:
    def __init__(self):
        # fonts
        self.font = pygame.font.SysFont(None, 32)
        self.smallFont = pygame.font.SysFont(None, 18)

        self.handCards = []

    def add_cards(self, card):
        self.handCards.append(card)
        
    def reposition_cards(self):
        # center cards along bottom of screen
        totalHandWidth = (len(self.handCards) * CARD_WIDTH) + ((len(self.handCards)-1) * CARD_SPACING)
        startX = (640 - totalHandWidth) // 2 #640 window width

        for index, card in enumerate(self.handCards):
            cardX = startX + (index * (CARD_WIDTH + CARD_SPACING))
            card.rect.x = cardX
            card.rect.y = HAND_Y_BASE

    def handle_mouse_move(self, mousePos):
        for card in self.handCards:
            if card.rect.collidepoint(mousePos):
                card.isHovered = True
            else:
                card.isHovered = False
                
    def handle_click(self, mousePos):
        for card in self.handCards:
            if card.rect.collidepoint(mousePos):
                card.isSelected = not card.isSelected
                print(f"Clicked {card.name}\nSelected: {card.isSelected}")

    def draw(self, surface):
        self.reposition_cards()
        for card in self.handCards:
            card.draw(surface, self.font, self.smallFont)