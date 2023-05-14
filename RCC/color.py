import numpy as np
import cv2


#기존 RGB(X) BGR(O) 
UltimateGary_color = (151, 149, 147) # O
Cerulean_color = (212, 183, 155) # O
GreenAsh_color = (173, 221, 160) # O
Illuminating_color = (77, 233, 245) # O
FrenchBlue_color = (181,114, 0) # O
IndigoBunting_color = (169, 108, 0) # O
Mint_color = (112, 161, 0)


img = np.zeros((450,450,3),np.uint8)
img = cv2.circle(img, (25, 25), 15, UltimateGary_color, -1)
img = cv2.circle(img, (60, 25), 15, Cerulean_color, -1)
img = cv2.circle(img, (95, 25), 15, GreenAsh_color, -1)
img = cv2.circle(img, (130, 25), 15, Illuminating_color, -1)
img = cv2.circle(img, (165, 25), 15, FrenchBlue_color, -1)
img = cv2.circle(img, (200, 25), 15, IndigoBunting_color, -1)
img = cv2.circle(img, (235, 25), 15, Mint_color, -1)
#-------------------------------------------------------------
PolatNight_color = (64, 53, 52)
Cerulean_color = (212, 183, 155)
UltimateGary_color = (151, 149, 147)
Willow_color = (79, 139, 154)
Illuminating_color = (77, 233, 245)
GreenAsh_color = (173, 221, 160)


img = cv2.circle(img, (25, 70), 15, PolatNight_color, -1)
img = cv2.circle(img, (60, 70), 15, Cerulean_color, -1)
img = cv2.circle(img, (95, 70), 15, UltimateGary_color, -1)
img = cv2.circle(img, (130, 70), 15, Willow_color, -1)
img = cv2.circle(img, (165, 70), 15, Illuminating_color, -1)
img = cv2.circle(img, (200, 70), 15, GreenAsh_color, -1)
#-------------------------------------------------------------
Inkweel_color = (69, 57, 54)
Cerulean_color = (212, 183, 155)
Willow_color = (79, 139, 154)
PickledPepper_color = (83, 166, 160)
IndigoBunting_color = (169, 108, 0)
PurpleRose = (202, 159, 176)


img = cv2.circle(img, (25, 115), 15, Inkweel_color, -1)
img = cv2.circle(img, (60, 115), 15, Cerulean_color, -1)
img = cv2.circle(img, (95, 115), 15, Willow_color, -1)
img = cv2.circle(img, (130, 115), 15, PickledPepper_color, -1)
img = cv2.circle(img, (165, 115), 15, IndigoBunting_color, -1)
img = cv2.circle(img, (200, 115), 15, PurpleRose, -1)
#-------------------------------------------------------------
Buttercream_color = (206, 227, 240)
PickledPepper_color = (83, 166, 160)
Cerulean_color = (212, 183, 155)
Macchiato_color = (117, 139, 173)

img = cv2.circle(img, (25, 160), 15, Buttercream_color, -1)
img = cv2.circle(img, (60, 160), 15, PickledPepper_color, -1)
img = cv2.circle(img, (95, 160), 15, Cerulean_color, -1)
img = cv2.circle(img, (130, 160), 15, Macchiato_color, -1)
#-------------------------------------------------------------
BabysBreath_color = (209, 226, 233)
UltimateGary_color = (151, 149, 147)
Cerulean_color = (212, 183, 155)
FrenchBlue_color = (181,114, 0)
PolatNight_color = (64, 53, 52)
Illuminating_color = (77, 233, 245)
GreenAsh_color = (173, 221, 160)

img = cv2.circle(img, (25, 205), 15, BabysBreath_color, -1)
img = cv2.circle(img, (60, 205), 15, UltimateGary_color, -1)
img = cv2.circle(img, (95, 205), 15, Cerulean_color, -1)
img = cv2.circle(img, (130, 205), 15, FrenchBlue_color, -1)
img = cv2.circle(img, (165, 205), 15, PolatNight_color, -1)
img = cv2.circle(img, (200, 205), 15, Illuminating_color, -1)
img = cv2.circle(img, (235, 205), 15, GreenAsh_color, -1)
#-------------------------------------------------------------
Macchiato_color = (117, 139, 173)
BabysBreath_color = (209, 226, 233)
Cerulean_color = (212, 183, 155)
Mint_color = (112, 161, 0)

img = cv2.circle(img, (25, 250), 15, Macchiato_color, -1)
img = cv2.circle(img, (60, 250), 15, BabysBreath_color, -1)
img = cv2.circle(img, (95, 250), 15, Cerulean_color, -1)
img = cv2.circle(img, (130, 250), 15, Mint_color, -1)
#-------------------------------------------------------------
Beige_color = (150, 185, 212)
DesertMist_color = (137, 181, 224)
Illuminating_color = (77, 233, 245)
UltimateGary_color = (151, 149, 147)
Cerulean_color = (212, 183, 155)
GreenAsh_color = (173, 221, 160)

img = cv2.circle(img, (25, 295), 15, Beige_color, -1)
img = cv2.circle(img, (60, 295), 15, DesertMist_color, -1)
img = cv2.circle(img, (95, 295), 15, Illuminating_color, -1)
img = cv2.circle(img, (130, 295), 15, UltimateGary_color, -1)
img = cv2.circle(img, (165, 295), 15, Cerulean_color, -1)
img = cv2.circle(img, (200, 295), 15, GreenAsh_color, -1)
#-------------------------------------------------------------
Sphagnum_color = (61,99,98)
Willow_color = (79, 139, 154)
BabysBreath_color = (209, 226, 233)
UltimateGary_color = (151, 149, 147)

img = cv2.circle(img, (25, 340), 15, Sphagnum_color, -1)
img = cv2.circle(img, (60, 340), 15, Willow_color, -1)
img = cv2.circle(img, (95, 340), 15, BabysBreath_color, -1)
img = cv2.circle(img, (130, 340), 15, UltimateGary_color, -1)
#-------------------------------------------------------------
Willow_color = (79, 139, 154)
BabysBreath_color = (209, 226, 233)
Macchiato_color = (117, 139, 173)
GreenAsh_color = (173, 221, 160)

img = cv2.circle(img, (25, 385), 15, Willow_color, -1)
img = cv2.circle(img, (60, 385), 15, BabysBreath_color, -1)
img = cv2.circle(img, (95, 385), 15, Macchiato_color, -1)
img = cv2.circle(img, (130, 385), 15, GreenAsh_color, -1)
#-------------------------------------------------------------
Cerulean_color = (212, 183, 155)
FrenchBlue_color = (181,114, 0)

img = cv2.circle(img, (25, 430), 15, Cerulean_color, -1)
img = cv2.circle(img, (60, 430), 15, FrenchBlue_color, -1)

cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()