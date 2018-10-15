﻿label alt_day4_sl_7dl_start:
    if herc or loki:
        $ routetag = "sl7dl_sport"
    else:
        $ routetag = "sl7dl"
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day4_sl_7dl_begin
    pause(1)
    call alt_day4_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day4_sl_7dl_loki_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day4_sl_7dl_herc_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_herc_evening
    else:
        call alt_day4_sl_7dl_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_evening
    pause(1)
    call alt_day4_sl_7dl_sundown
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_7dl_sleeptime
    pause(1)
    jump alt_day5_sl_7dl_start

label alt_day5_sl_7dl_start:
    if herc and alt_day4_sl_7dl_workout :
        $ routetag = "sl7dl_sport"
    call alt_day5_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day5_sl_7dl_begin
    pause(1)
    call alt_day5_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
    elif herc:
        $ routetag = "sl7dl_herc"
    call alt_day5_sl_7dl_candle
    pause(1)
    if loki:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_loki_evening
    elif herc:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_herc_evening
        pause(1)
    else:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_evening
    pause(1)
    $ alt_chapter(5, u"Славя. 7ДЛ. Костёр")
    call alt_day5_sl_7dl_campfire
    pause(1)
    if herc and (lp_sl > 16) and (persistent.sl_7dl_good_loki and persistent.sl_7dl_good):
        call alt_day5_sl_7dl_hentai
        $ alt_day5_sl_7dl_hentai_done = True
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_sl_7dl_sleeptime
    pause(1)
    window hide
    with fade
    jump alt_day6_sl_7dl_start

label alt_day6_sl_7dl_start:
    if herc:
        call alt_day6_sl_7dl_camping
        pause(1)
        call alt_day6_sl_7dl_revenge
    if not alt_day5_sl_7dl_herc_sick:
        $ routetag = "sl7dl_sport"
    call alt_day6_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day6_sl_7dl_begin
    pause(1)
    if not alt_day5_sl_7dl_herc_sick:
        call alt_day6_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day6_sl_7dl_loki_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_loki_day
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day6_sl_7dl_herc_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_herc_day
    else:
        $ routetag = "sl7dl"
        call alt_day6_sl_7dl_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_day
        pause(1)
    call alt_day6_sl_7dl_evening
    pause(1)
    call alt_day6_sl_7dl_catapult
    if (karma < 50) and not herc:
        pause(1)
        return
    pause(1)
    if (herc or loki) or alt_day5_sl_7dl_olroad:
        $ routetag = "sl7dl_dress"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Дискотека")
    call alt_day6_sl_7dl_disco
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if persistent.sl_7dl_good_loki or persistent.sl_7dl_good_herc or persistent.sl_7dl_good:
        $ routetag = "sl7dltrue"
    elif (lp_sl >= 19) and (karma > 120):
        $ routetag = "sl7dlgood"
        pause(1)
    elif lp_sl >= 19:
        $ routetag = "sl7dlneu"
    else:
        $ routetag = "sl7dlbad"
    if lp_sl >= 19:
        if alt_day6_sl_7dl_forgive or not loki:
            call alt_day6_sl_7dl_hentai
            $ alt_day6_sl_7dl_hentai_done = True
    pause(1)
    if not alt_day6_sl_7dl_hentai_done or not (herc or loki):
        call alt_day6_sl_7dl_sleeptime
    pause(1)
    jump alt_day7_sl_7dl_start

label alt_day7_sl_7dl_start:
    call alt_day7_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day7_sl_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_sl_7dl_packing
    pause(1)
    $ alt_chapter(7, u"Славя. 7ДЛ. Отъезд")
    call alt_day7_sl_7dl_leaving
    pause(1)
    if routetag == "sl7dltrue":
        $ persistent.sprite_time = "sunset"
        $ prolog_time()
        $ alt_chapter(6, u"Славя. 7ДЛ. Тру")
        call alt_day7_sl_7dl_true
        pause(1)
        return
    $ alt_chapter(7, u"Славя. 7ДЛ. Эпилог")
    if loki:
        call alt_day7_sl_7dl_loki_epilogue
    elif herc:
        call alt_day7_sl_7dl_herc_epilogue
    else:
        call alt_day7_sl_7dl_epilogue
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ prolog_time()
    if lp_sl > 20:
        if herc and alt_day4_sl_7dl_phone:
            call alt_day7_sl_7dl_mistique
            pause(1)
            if routetag == "sl7dlgood":#Все внутренние инструкции на 50 строчек необходимо перенести в од.
                call alt_day7_sl_7dl_mistique_good
            else:
                call alt_day7_sl_7dl_mistique_bad
        elif herc:
            call alt_day7_sl_7dl_unmistique
            pause(1)
            if routetag == "sl7dlgood":
                call alt_day7_sl_7dl_unmistique_good
            else:
                call alt_day7_sl_7dl_unmistique_bad
        elif loki and alt_day6_sl_7dl_forgive:
            call alt_day7_sl_7dl_dam
            pause(1)
            if routetag == "sl7dlgood":
                call alt_day7_sl_7dl_dam_good
            else:
                call alt_day7_sl_7dl_dam_bad
        elif loki:
            call alt_day7_sl_7dl_jerc
            pause(1)
        else:
            if alt_day5_sl_7dl_olroad:
                call alt_day7_sl_7dl_loop
            else:
                call alt_day7_sl_7dl_loopback
    else:
        call alt_day7_sl_7dl_bad
    pause(1)
    return