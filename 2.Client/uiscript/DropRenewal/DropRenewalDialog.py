"""
	Author	: Valiant
	File	: DropRenewalDialog.py
	Date	: 2019.08.27
"""

import uiScriptLocale, localeInfo

DROP_RENEWAL_PATH = [
	"d:/ymir work/ui/public/middle_button_01.sub",
	"d:/ymir work/ui/public/middle_button_02.sub",
	"d:/ymir work/ui/public/middle_button_03.sub"]

DROP_RENEWAL_SLOT	= "d:/ymir work/ui/public/Slot_Base.sub"
DROP_RENEWAL_WIDTH	= 290
DROP_RENEWAL_HEIGHT	= 115

window = {
	"name" : "DropRenewalDialog",
	"style" : ("movable", "float",),
	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,
	"width" : DROP_RENEWAL_WIDTH,
	"height" : DROP_RENEWAL_HEIGHT,
	"children" :
	(
		{
			"name" : "DropRenewalBoard",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : DROP_RENEWAL_WIDTH,
			"height" : DROP_RENEWAL_HEIGHT,
			"children" :
			(
				{ "name" : "MessageBoxThree",	"type" : "text","x" : -10,"y" : 20,"horizontal_align" : "center","text" : localeInfo.DROP_RENEWAL_MESSAGE,"text_horizontal_align" : "center","text_vertical_align" : "center",},
				{ "name" : "MessageBox",		"type" : "text","x" : -10,"y" : 35,"horizontal_align" : "center","text" : uiScriptLocale.MESSAGE,"text_horizontal_align" : "center","text_vertical_align" : "center",},
				{ "name" : "MessageBoxTwo",		"type" : "text","x" : -10,"y" : 55,"horizontal_align" : "center","text" : uiScriptLocale.MESSAGE,"text_horizontal_align" : "center","text_vertical_align" : "center",},
				{
					"name" : "DropButton",
					"type" : "button",
					"x" : -110,
					"y" : DROP_RENEWAL_HEIGHT-35,
					"horizontal_align" : "center",
					"text" : localeInfo.DROP_RENEWAL_DROP,
					"default_image"	: DROP_RENEWAL_PATH[0],
					"over_image"	: DROP_RENEWAL_PATH[1],
					"down_image"	: DROP_RENEWAL_PATH[2],
				},
				{
					"name" : "DestroyButton",
					"type" : "button",
					"x" : -50,
					"y" : DROP_RENEWAL_HEIGHT-35,
					"horizontal_align" : "center",
					"text" : localeInfo.DROP_RENEWAL_DESTROY,
					"default_image"	: DROP_RENEWAL_PATH[0],
					"over_image"	: DROP_RENEWAL_PATH[1],
					"down_image"	: DROP_RENEWAL_PATH[2],
				},
				{
					"name" : "SellButon",
					"type" : "button",
					"x" : 10,
					"y" : DROP_RENEWAL_HEIGHT-35,
					"horizontal_align" : "center",
					"text" : localeInfo.DROP_RENEWAL_SELL,
					"default_image"	: DROP_RENEWAL_PATH[0],
					"over_image"	: DROP_RENEWAL_PATH[1],
					"down_image"	: DROP_RENEWAL_PATH[2],
				},
				{
					"name" : "CancelButton",
					"type" : "button",
					"x" : 70,
					"y" : DROP_RENEWAL_HEIGHT-35,
					"horizontal_align" : "center",
					"text" : localeInfo.DROP_RENEWAL_CLOSE,
					"default_image"	: DROP_RENEWAL_PATH[0],
					"over_image"	: DROP_RENEWAL_PATH[1],
					"down_image"	: DROP_RENEWAL_PATH[2],
				},
				{
					"name" : "ItemSlot",
					"type" : "slot",
					"x" : 250,
					"y" : 9,
					"width" : 32,
					"height" : 200,
					"horizontal_align" : "center",
					"image" : DROP_RENEWAL_SLOT,
					"slot" : (
						{"index":0, "x":0, "y":0, "width":32, "height":32},
						{"index":1, "x":0, "y":33, "width":32, "height":32},
						{"index":2, "x":0, "y":66, "width":32, "height":32},
					),
				},
			),
		},
	),
}
