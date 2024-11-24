import random

location_data: dict[str, dict[str, dict[str, tuple[str, str, str]]]] = {
    "🎬 Кино" : {
        "🎬 Боевик": {
            "1": ("https://avatars.mds.yandex.net/get-afishanew/4395007/0e6bed99-8e30-42aa-8c46-4fd52c4d93c7/s190x280","Хищные земли, Триллер, Боевик, Фантастика, 16+","https://clck.ru/3EnWHv"),
            "2": ("https://avatars.mds.yandex.net/get-afishanew/21626/0bb3407019ab4c6022a0cacf97f97b84/s190x280","Гладиатор, Приключения, Боевик, История, Драма, 16+","https://clck.ru/3EnWJp"),
            "3": ("https://avatars.mds.yandex.net/get-afishanew/5098259/0711ab4e-176d-42b9-8410-86086f55b2d6/s190x280","Непробиваемые, Триллер, Криминальный, Боевик, 18+","https://clck.ru/3EnWLz")
        },
        "🎭 Комедия": {
            "1":("https://avatars.mds.yandex.net/get-afishanew/5109582/43d0e1a5-46df-4c6b-9e75-0b2f49411978/s190x280","Зять, Комедия, Мелодрама, 16+","https://clck.ru/3EnWMz"),
            "2":("https://avatars.mds.yandex.net/get-afishanew/4395007/41f7390e-5829-43f3-bb98-d7fdb831554b/s190x280","Манюня: Приключения в деревне, Комедия, Приключения, Детям, Семейное кино, 6+","https://clck.ru/3EnWPT"),
            "3":("https://avatars.mds.yandex.net/get-afishanew/5098259/95218c99-6ea8-44bd-95a6-386bf5cdd4b5/s190x280","Возвращение попугая Кеши, Комедия, Семейное кино, Детям, 6+","https://clck.ru/3EnWPx")
        },
        "👻 Хоррор": {
            "1":("https://avatars.mds.yandex.net/get-afishanew/4395007/4085b71d-c2f8-4a2d-b3b1-893bb0036028/s190x280","Еретик, Ужасы, Триллер, 18+","https://clck.ru/3EnWR5"),
            "2":("https://avatars.mds.yandex.net/get-afishanew/5109582/093d74d0-f645-4545-ab76-f5775c6c373e/s190x280","Субстанция, Ужасы, Драма, Авторское кино, 18+","https://clck.ru/3EnWRi"),
            "3":("https://avatars.mds.yandex.net/get-afishanew/4768735/60e3d337-a7c8-4311-b709-31fb26e71b01/s190x280","Реинкарнация. Возвращение ведьмы, Ужасы, 18+","https://afisha.yandex.ru/omsk/cinema/reinkarnatsiya-vozvrashcheniye-vedmy?source=rubric&schedule-preset=tomorrow")
        },
        "🚀 Фантастика": {
            "1":("https://avatars.mds.yandex.net/get-afishanew/4395007/0e6bed99-8e30-42aa-8c46-4fd52c4d93c7/s190x280","Хищные земли, Фантастика, Триллер, Боевик, 16+","https://clck.ru/3EnWSd"),
            "2":("https://avatars.mds.yandex.net/get-afishanew/4768735/588a054c-67be-4004-b6c5-d5fec32b66a9/s190x280","УничтоЖанна, Приключения, Комедия, Фантастика, 16+","https://clck.ru/3EnWTL"),
            "3":("https://avatars.mds.yandex.net/get-afishanew/4395007/8d4767dd-2ed9-4435-b171-6be786600c3e/s190x280","Бернард: миссия Марс, Мультфильм, Приключения, Детям, Фантастика, Комедия, Семейное кино, 6+","https://avatars.mds.yandex.net/get-afishanew/4395007/8d4767dd-2ed9-4435-b171-6be786600c3e/s190x280")
        }
    },
    "🎤 Концерты": {
        "🎤 Поп": {
            "1":("https://avatars.mds.yandex.net/i?id=ca0ef4bf0862bf188d7f7c809d6f141e_l-11944703-images-thumbs&n=13","Zoloto, Ангар, Поп, Инди, 16+","https://afisha.yandex.ru/omsk/concert/zoloto-tour?source=rubric"),
            "2":("https://cdni-vm.servicecdn.ru/2020.11/original/1200_5fae809882682c3ecdc16a6e.jpg","Ева Польна, Филармония. Концертный зал, Поп, 6+","https://afisha.yandex.ru/omsk/concert/eva-polna-v-storonu-serdtsa?source=rubric"),
            "3":("https://cdn.culture.ru/images/ce0d863a-7992-573e-aa1a-770b1b017890","Руки Вверх!, G-Drive Арена, Поп, 12+","https://afisha.yandex.ru/omsk/concert/ruki-vverkh-2022-11-20?source=rubric")
        },
        "🎧 Реп": {
            "1":("https://i.pinimg.com/736x/cc/9f/47/cc9f473d81d47a97552977b6fa292792.jpg","Toxi$, Ангар, Хип-хоп и рэп, 16+","https://afisha.yandex.ru/omsk/concert/toxi-tour?source=rubric"),
            "2":("https://go.zvuk.com/imgs/2022/06/28/18/5471357/8700feb5618bf388089e97d59f90b99879ab7d27.jpg","Friendly Thug 52 Ngg, Ангар,Хип-хоп и рэп, 16+","https://afisha.yandex.ru/omsk/concert/friendly-thug-52-ngg-tour?source=rubric"),
            "3":("https://avatars.mds.yandex.net/i?id=495e9e1cce3982ab8fe5e589b24f0b45_l-5690699-images-thumbs&n=13","CMH, Ангар,Хип-хоп и рэп, 16+","https://afisha.yandex.ru/omsk/concert/cmh-tour?source=rubric")
        },
        "🎷 Джаз": {
            "1":("https://cdn.culture.ru/images/a7593ab8-6141-5604-9f2c-4a8ad8fea2ee","Денис Мацуев. От классики до джаза, Филармония. Концертный зал,Джаз и блюз, Классическая музыка, 12+","https://afisha.yandex.ru/omsk/concert/denis-matsuyev-ot-klassiki-do-dzhaza?source=rubric"),
            "2":("https://avatars.mds.yandex.net/get-afishanew/5109582/3a99326402e6a0ea558290287d2e5f09/960x690_noncrop","Funk Power. Ритмы соула, хип-хопа и фанка, Oldman Pub, Джаз и блюз, Фанк, Соул, 12+","https://afisha.yandex.ru/omsk/concert/funk-power-ritmy-soula-khip-khopa-i-fanka?source=rubric"),
            "3":("https://cdn.culture.ru/images/3f10c9ac-f88a-5f7f-9e78-bf92a9ec1868","J. Seven, Birliman, Поп, Рок, Джаз и блюз, 12+","https://afisha.yandex.ru/omsk/concert/j-seven-kontsert-romanticheskoi-saksofonnoi-muzyki?source=rubric")
        },
        "🎻 Классическая музыка": {
            "1":("https://mos-mmdm.com/store/1/66/o_prev_8783_1682428982.jpg","Оркестр CAGMO. Саундтреки Эйнауди. Концерт при свечах, Концерт-холл РЦСО, Шоу, Неоклассика, Саундтрек, Классическая музыка, 6+","https://afisha.yandex.ru/omsk/concert/orkestr-cagmo-saundtreki-eynaudi-kontsert-pri-svechakh?source=rubric"),
            "2":("https://avatars.mds.yandex.net/i?id=f073967999ef8a4e1028e94f45f5ae4a_l-5220417-images-thumbs&n=13","Денис Мацуев. Виртуозы с оркестром, Филармония. Концертный зал, Классическая музыка, 12+","https://afisha.yandex.ru/omsk/concert/denis-matsuev-virtuozy-s-orkestrom?source=rubric"),
            "3":("https://yandex-images.clstorage.net/vTb95A401/a6ced2f7Z/o5TGVOQ-jNSCH3dUblZt5CLIvxdXfeHiCl0imKHkd2l-qCmFa65wBEWHknvTTGkX4_yGs5U1FzjO7yButfmj6aqtjg3VM4Cl50Z3CUNmccAytZNid3z9k0JxfvS0nVNYGpQhqMYO4eTVbk_vcrTY4sq53_LVQWYxy0aBd_w0E70L1Pq0oFol3GqHfsSm7v1YJulfcxN8DfOSRSvUlOGGkJNVXFD-VqkITUJLH15MaP469UNG1cjKVTMuQFvogN8pE4TKnHCyJWh6Hwqsnoqx-P6VS-93hBnbSuGvUJzNqjjjNbh0HtLZTHnOp69GLHReHg3Tgtl0_klXZkAjkFhzybeQymCEPgUMiovmpCYanWgitU9PU_y1WxLRozTY-UqM-znIDKpGtaDZXmd7ljSgFs55Ky5hbNL9w35QvzQcc71DyKIgOOJFtJJreuBanr2sCj2Tt0fIxW9KyS9E-AFGFDPleHh-JiHsAZ6nD0o0bGZ6cb_meThaqScCODew0Fd1o2Ry7PBi3Qiabz7YGuaZ0H65E-cngO17HjWjTNARcoyPrVjIGtJJVH2Wx8_enHRWYomDOtWw8sWneiAnpGB__U_U1gzQbt14plOW4DLqWeSqBdu_U5iNl-Yp20j0tXaIf018LJbqeTzlMndD3hCo3v5910rxPL6pX3bsf2wgA8U3bJJQcMIJ9HrL3mQu8nk4kv3fa48MlX-STavUKJmK9J-lTGDy4uEImVbvfzIMOLrGZe8KkTjCSY8mXEu4JJPpF4Qa4Dw2STy-EzJwzrZ1JDKxi3tLSL3j_vGP-DilXuxDKSR0slpRrJmq-5vaBOh68iVvLtkYzlE7ekhrXKTfzTPA4pB4yg2oppOyXA4WgdDi4QNLn2BFG96du_iQAdoM62nEXNJC1bQBgjcLvuxQav4B8_qplBJ9E_6UT2SIV807SM6sfCZNDO6_DjCCgjXEJjXHN8sQ1VOi_ZNYvIWo","Concord Orchestra. Симфонические рок-хиты «Человек будущего», Цирк, Шоу, Рок, Классическая музыка, 12+","https://afisha.yandex.ru/omsk/concert/concord-orchestra-simfonicheskie-rok-khity-chelovek-budushchego?source=rubric")
        }
    },
    "🎭 Театр":{
        "🎭 Комедия": {
            "1":("https://i.ytimg.com/vi/HjyEofSruC4/maxresdefault.jpg","Чай с мятой и лимоном, Комедия, 12+","https://afisha.yandex.ru/omsk/theatre_show/chai-s-miatoi-i-limonom?source=rubric"),
            "2":("https://янтарьхолл.рф/upload/iblock/e2e/c9wxdmrerxy0ktt3at0xl6s5wyvuxoa9.jpg","Палата бизнес-класса, Музыкальный театр, Комедия, 16+","https://afisha.yandex.ru/omsk/theatre_show/palata-biznes-klassa-antrepriza?source=rubric"),
            "3":("https://yandex-images.clstorage.net/vTb95A401/a6ced2f7Z/o5TGVOQ-jNSCH3dUblZt5CLIvxdXfeHiCl0imfHMS1Qr5XWALvcsNE2Hom6ffG0__9yCu4BFPn2S_zUnCIH2tOqFo1G1M_XIggsmeEdmBdRinY9iWyjphhpARqn8Ve6wp2mYWPJW-cTl9vcfxjwdYubpGx_BKNqpxxZkT0Tw7wGXEEpASNp9RBoferRWAgUkAk27N3sIlVPSyYfUBG22-EvxtFwCegF0-Qa7g3I8lM6CEXPe7TxuZVMONH9sIAcBIwDSNCDiGQi6xwagymb9MCqVH7P_ALl_ernnMCCNMogPxTiwsmJhaFkiQxO2MCj6nnU73pVEtsmzqiB_kNSLIUfwRtgoWokkKhsmpGpChZyqzS-_m0SNn86h60BYOabk42WocGayebwR8jfrGogw1irhI84J4PLJx154F9BoV2H_6KZEbCYNBO4zrniSVrHsnpU3M-tkdZNWaTfwLO3GcK-9aLASbnlwYUY_f9KQZF5-BV-mgWQ-7Q--1MccoNf5Q-CiAFRmdSCSRyr4wjb5xIrBy7_jTGWnztV_0JyJMhgXwWDQ0vrRaFFex0MOPOz2EoUnvpFwjsWHUmRj_IDb-TPcnqhsTnngppOWMJpC4aRmOdfH52jBo8oln_R4BQoof1nEYF76XbTZwjMXfhhgun59K3LJuM65vyrcJ6Agdy2_AAbg6FJhwHqrbjROnnW8jk2zt3u07V-2xXfENGECsEsloPhiFkEkvforLz54ZMaerXvC_WzKKZMKNK8QbINtd8TeDPyyJcxmCyJgXloxlBIhD5NXpNGLrhn7rCAhugDvJVzshv5J9H3Oa68aMETKhhkn1t2ISmW3LnBXYCh_KePcXozQcoU4ktty6G6OGWzqAWOnVwx1D06xu0wIQaKE9710IBaaoUxtwk8zzkDIFqoxowr5sGbttyb4e1wsk2lHlHIwvP4RjIYfpiwS2mn8on0Dj_cg8X-6TTvENAnU","Вор моей дочери, Дом актёра, Комедия, 12+","https://afisha.yandex.ru/omsk/theatre_show/vor-moei-docheri-antrepriza?source=rubric")
        },
        "🩰 Балет": {
            "1":("https://avatars.mds.yandex.net/i?id=fb1304faba486fa2b01250839cf33f37_l-5888429-images-thumbs&n=13","Лебединое озеро, Музыкальный театр, Балет, 12+","https://afisha.yandex.ru/omsk/ballet/lebedinoye-ozero-muzykalnyi-teatr?source=rubric"),
            "2":("https://yandex-images.clstorage.net/vTb95A401/a6ced2f7Z/o5TGVOQ-jNSCH3dUblZt5CLIvxdXfeHiCl0imf3IVjwmpCmoM6pwPQzO_y6XSR0Cp_iv-sx9Fxja6yBjCIH2sOqNk1mxE_XIggsmeEdmBdRinY9iWyjphhpARqn8Ve6wp2mYWPJW-cTl9vcfxjwdYubpGx_BKNqpxxZkT0Tw7wGXEEpASNp9RBoferRWAgUkAk27N3sIlVPSyYfUBG22-EvxtFwCegF0-Qa7g3I8lM6CEXPe7TxuZVMONH9sIAcBIwDSNCDiGQi6xwagymb9MCqVH7P_ALl_ernnMCCNMogPxTiwsmJhaFkiQxO2MCj6nnU73pVEtsmzqiB_kNSLIUfwRtgoWokkKhsmpGpChZyqzS-_m0SNn86h60BYOabk42WocGayebwR8jfrGogw1irhI84J4PLJx154F9BoV2H_6KZEbCYNBO4zrniSVrHsnpU3M-tkdZNWaTfwLO3GcK-9aLASbnlwYUY_f9KQZF5-BV-mgWQ-7Q--1MccoNf5Q-CiAFRmdSCSRyr4wjb5xIrBy7_jTGWnztV_0JyJMhgXwWDQ0vrRaFFex0MOPOz2EoUnvpFwjsWHUmRj_IDb-TPcnqhsTnngppOWMJpC4aRmOdfH52jBo8oln_R4BQoof1nEYF76XbTZwjMXfhhgun59K3LJuM65vyrcJ6Agdy2_AAbg6FJhwHqrbjROnnW8jk2zt3u07V-2xXfENGECsEsloPhiFkEkvforLz54ZMaerXvC_WzKKZMKNK8QbINtd8TeDPyyJcxmCyJgXloxlBIhD5NXpNGLrhn7rCAhugDvJVzshv5J9H3Oa68aMETKhhkn1t2ISmW3LnBXYCh_KePcXozQcoU4ktty6G6OGWzqAWOnVwx1D06xu0wIQaKE9710IBaaoUxtwk8zzkDIFqoxowr5sGbttyb4e1wsk2lHlHIwvP4RjIYfpiwS2mn8on0Dj_cg8X-6TTvENAnU","Жизель, Музыкальный театр, Балет, 12+","https://afisha.yandex.ru/omsk/ballet/zhizel-omskii-gosudarstvennyi-muzykalnyi-teatr?source=rubric"),
            "3":("https://cdn-storage-media.tass.ru/resize/976x648/tass_media/2024/02/12/8/1707744167600845_86vP_1Ag.jpg","Идиот, Музыкальный театр, Балет, 12+","https://afisha.yandex.ru/omsk/ballet/idiot-omskiy-muzykalnyy-teatr?source=rubric")
        },
        "🎶 Опера": {
            "1":("https://otvet.imgsmail.ru/download/3659816_bec9d93b86dd50e367d8d96d98839695_800.jpg","Свадьба Фигаро, Музыкальный театр, Опера, 12+","https://afisha.yandex.ru/omsk/opera/svadba-figaro-omskii-muzykalnyi-teatr?source=rubric"),
            "2":("https://cdn.culture.ru/images/4fb98880-8fa3-5b01-800a-2fd82807fae4","Евгений Онегин, Музыкальный театр, Опера, 12+","https://afisha.yandex.ru/omsk/opera/evgeniy-onegin-omskiy-muzykalnyy-teatr?source=rubric"),
            "3":("https://avatars.mds.yandex.net/i?id=a269a7ab6c7367b4986849dde44f35fbbe4a2b1c-5232021-images-thumbs&n=13","Пиратский треугольник, Музыкальный театр, Опера, 12+","https://afisha.yandex.ru/omsk/opera/piratskii-treugolnik-omskii-muzykalnyi-teatr?source=rubric")
        },
        "🌟 Мюзикал": {
            "1":("https://avatars.mds.yandex.net/i?id=5d9fc4c50f280016cb5a6e5fb9354460_l-4438551-images-thumbs&n=13","Любовь под прикрытием, Музыкальный театр, Мюзикл, Комедия, 12+","https://afisha.yandex.ru/omsk/musical/liubov-pod-prikrytiem-muzykalnyi-teatr?source=rubric"),
            "2":("https://yandex-images.clstorage.net/vTb95A401/a6ced2f7Z/o5TGVOQ-jNSCH3dUblZt5CLIvxdXfeHiCl0imL35AiQytDWsI5M1dFma-n62MHUP9qSv950pAzz6-zkSsejaob_Y2hXVJ4ip01p3CT52YfAqvcobEwyJ8340K-iE6H4NVqQoGMZ24eihLjuDSozEPqqF9_agGBYtY0d8f3Bgm0m_9HJEzJLxMD5LksC2-vnkdnHbfxP86SNKYQvI-D22hJfZ0CCePg1wjSrLr7I82M7mGUP2KbRy1QuGUGvErA9R78RalCSSRSCmP_r40rZZPAplRxvr6MH77uWPwNQRHvT3PfTAGk5JRAHGe7fSIHjqHomH-pWAbrFDhigTHADv9fvEpmCosiHQMtPyQEKayeAqYec_k0RBo97p64Tg8ars-02MdI4ipeSRBq9nyvQwOmpxK0KNrNolW5a0t1gAmwGjrObcdPKZyNJPtjzGug3Ior0fK6c0dfvGZZukGP0yJCf9-KDutuk8Ucbbu8o4QI5i5eNa2SSOwSf-PDOUJFPhD3wqFPRqJcDWC458vp5xvCY9T0vvHGGvOumTjAjJqphv3UjEGt5RQFmmGy9iIHCWmtk_9lGM4kFf5iwnJAzbDb_YyjT4alX86qO2VLJeRWia9Rc_93yNVyaRl6isza5oj_msSCLuOdj9Fpcv7vz4Cm6NT9LdwI65Uyp072Rw43UHnJaUVL7ZIHLrMkiqfplQYvHD42NkZSNC4Qt0gDHSiGfJ4Cwqdg2kmY6rw_JsnDJ2tQ-y2bxuaQOaQDtg4M9V7xQm2KD-EeSqByao7nKF8C6l0ycnTPlP_sUnZLzlylTrofRsksappGWaTyv6vFwGNjUr-vmwdt1fjmDf4KzrcavsVpxcuoX8KocKaE6GcSB-LePzD7QBb5LxJ8wYYSr8q0HcDIpCsTxNVt9PEgRMChKp_4p1bFr121JE58wk63kjwGqYsPohtAY7ZuTaMmXkqumfp38kSRPy2YfgnBHc","Алые паруса, Музыкальный театр, Мюзикл, 12+","https://afisha.yandex.ru/omsk/musical/alyye-parusa-omskiy-gosudarstvennyy-muzykalnyy-teatr?source=rubric"),
            "3":("https://ponominalu.ru/media/i/536x360/55-c8-55c8b282a0f2d636ba9eea7a6150b242.jpg","Дракула. У вечности в плену, ГЦНТ. Дворец им. Малунцева, Мюзикл, 16+","https://afisha.yandex.ru/omsk/musical/drakula-u-vechnosti-v-plenu-antrepriza?source=rubric")
        }
    },
    "🖼️ Выставка":{
        "🖼️ Живопись": {
            "1":("https://yandex-images.clstorage.net/vTb95A401/a6ced2f7Z/o5TGVOQ-jNSCH3dUblZt5CLIvxdXfeHiCl0imL3xB2lusX2gIuMgKETHoy6fTGxf59y-o4UpBx2Xsyh6pLWn_a6A10TwY4Ckr2s3JT8XFLF74NpKBhj583JlJ6GE-TJgF-kp_D7GJAxk57ZrKtT43iZBWyplvPrB-75EZ-DR-63zMD8E6PIRtBoXAtxKfrHE6iHDh--QdWtmOeuw4PnCAMfdfNweuvHE7SbLkxKMsDK-bV_aSURK3Qvy2NPgWFfJC1j-KPxG3SACRzL0mpaxcPq5t-_X9DnLvkX_LIQB1igfefhYFpbdbJ1GL7fyCMB2iuGzalEkVn0vCkgX7ORj1W8Q_lCEnnHAplMyCG4akRQKLVvnb2QVW2Jl-4ygeXqoR0n0PFKiPdiFSl_PRpysmipxc76BPII1_36wu1T8T2H7CO7MINpxtFILWkjSxtGsEs3HoxPgNZ9K7Sd0tE0KnB9ReExyWjFATZbvu5L8ONbysbPKXTxORUt2JHNMqMc1H3SGRKQWVXyyp4qEGkZJEBrJg5tTmBHjPmmnJNQFIohLrfREWkoF2PHezwv2CFBujrnTCsmUVnVTjhiv4CBvWZ8MnlSwpn30XhcuZDpKSWAm9Suje5TR1-rVb3ygHUJks7GMQH7uAdwBPuvvejBgBhYdY4bJGIr9z3pM38SsIzVnAFIMeOYBzCavajia5p3s-m1jJ2eM8QvSLWuofIlajMfV_Nyiwv2g4dbbox44-DJqefu6JQQamfdidJ-kqF_Vt1DiOKzikeAGR-KI1hLdJD61jzOHyP0XcmE_uLjNchCradjwsv4puD1as7degEiWaoXvXs0MylnDIvS77IhTzQMM9hhIYt3EIgMa-JLumbAmNQ8fR2gJ46Ixt4hs5YroiwXs8BparViVGlOfPpjMjvKtI86p5HJJzwZob5wEj-EriCo8cE5VxCqLNsSWAtkUbhmzc8v8vfdm5XP0OJUY","Владеть ценным сокровищем, Музей им. Врубеля, Живопись, 0+","https://afisha.yandex.ru/omsk/art/vladet-tsennym-sokrovishchem-russkii-risunok-i-akvarel-xviii-nachala-xx-veka-kazachestvo-iz-sobraniia-gosudarstvennogo-russkogo-muzeia?source=rubric"),
            "2":("https://avatars.mds.yandex.net/i?id=c4f1f6f573032514d96e36c79c27dfec_l-9570000-images-thumbs&n=13","Постоянная экспозиция. 2 этаж, Музей им. Врубеля, Живопись, 6+","https://afisha.yandex.ru/omsk/art/postoiannaia-ekspozitsiia-2-etazh?source=rubric"),
            "3":("https://avatars.mds.yandex.net/i?id=8337154c9ee7901022633b300cddd65d_l-4349375-images-thumbs&n=13","Пётр I и его эпоха. Из собрания Государственного Эрмитажа, Музей им. Врубеля. Эрмитаж-Сибирь, История, Живопись, 6+","https://afisha.yandex.ru/omsk/art/petr-i-i-ego-epokha-iz-sobraniia-gosudarstvennogo-ermitazha?source=rubric")
        },
        "📜 История": {
            "1":("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPzdhma6ubFzdDs4cLNQPSiM1EccxY4UmjpA&s","Сибирский град Петров, Историко-краеведческий музей, История, Детям, 0+","https://afisha.yandex.ru/omsk/art/sibirskii-grad-petrov-2024?source=rubric"),
            "2":("https://admomsk.ru/image/image_gallery?uuid=b9ebd23b-8532-4c23-bce6-1cd9297c2230&groupId=14&t=1448879107486","Выставки музея «Искусство Омска», Искусство Омска, История, Искусство, 0+","https://afisha.yandex.ru/omsk/art/vystavki-muzeia-iskusstvo-omska?source=rubric"),
            "3":("https://afisha-omsk.ru/media/events/2024/10/22/10d3c4af913fe7cd154d31a19b5a3882.1024.jpg","Пётр I и его эпоха. Из собрания Государственного Эрмитажа, Музей им. Врубеля. Эрмитаж-Сибирь, История Живопись 6+","https://afisha.yandex.ru/omsk/art/petr-i-i-ego-epokha-iz-sobraniia-gosudarstvennogo-ermitazha?source=rubric")
        },
        "🏎️ Авто-мото": {
            "1":("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQ4KQ1vGS1rM8d4Md4YNwXPPT38WoWBfEjug&s","Оружие Победы, Музейный комплекс воинской славы омичей, Выставка, На воздухе, История, Детям, 0+","https://afisha.yandex.ru/omsk/art/oruzhiye-pobedy-muzeinyi-kompleks-voinskoi-slavy-omichei?source=rubric")
        },
        "🖌️ Прикладное искусство": {
            "1":("https://kultura55.ru/sites/default/files/styles/gallery_watermark/public/dsc_0608_4.jpg?itok=GuhetUoU","Япония. Красота повседневности, Музей им. Врубеля, Прикладное искусство, 0+","https://afisha.yandex.ru/omsk/art/iaponiia-krasota-povsednevnosti?source=rubric"),
            "2":("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTodojOpKzbGHQ--Tl0JgYrr0oMlUg2AphsdQ&s","Микромир Анатолия Коненко, Музей им. Врубеля, Искусство, Прикладное искусство, Детям, 0+","https://afisha.yandex.ru/omsk/art/mikromir-anatoliia-konenko-2024?source=rubric"),
            "3":("https://s4.afisha.ru/mediastorage/04/0c/cdd32ac6007e4d779c4714ac0c04.jpg","Золотая кладовая, Музей им. Врубеля, Прикладное искусство, История, 0+","https://afisha.yandex.ru/omsk/art/zolotaia-kladovaia-omsk?source=rubric")
        }
    },
    "🚶 Экскурсии":{
        "История и искусство": {
            "1":("https://afisha-omsk.ru/media/events/2024/03/01/3522837d26271d870df0a71da1421685.1024.jpg","Следующая остановка, Трамвайная остановка «Трамвайное депо», Экскурсия, Иммерсивный театр, Аудиоспектакль, Аудиогид, Иммерсивная экскурсия, 12+","https://afisha.yandex.ru/omsk/excursions/sleduiushchaia-ostanovka?source=rubric"),
            "2":("https://afisha-omsk.ru/media/events/2024/03/17/b5832369ab64cebae8163bf01ef9385a.1024.jpg","Волшебные потеряшки, Арлекин, Детям, Интерактив, Искусство, 6+","https://afisha.yandex.ru/omsk/excursions/volshebnye-poteriashki?source=rubric"),
            "3":("https://static.gorodzovet.ru/uploads/2024/8/23/photo600-10236493.jpg?v=032024","Жемчужины Омского музея, Историко-краеведческий музей, Выставка, По музеям, История, 0+","https://afisha.yandex.ru/omsk/excursions/zhemchuzhiny-omskogo-muzeia?source=rubric")
        }
    }

}



activities = {
    "🎲 Настольные игры": {
        "Описание": "Соберитесь всей семьей и играйте в настольные игры.",
        "Идеи": [
            "Сыграйте в классическую игру, такую как Монополия или Уно.",
            "Попробуйте новые настольные игры, такие как Колонизаторы или Диксит.",
            "Устроить турнир с призами для победителей."
        ]
    },
    "🍽️ Кулинарный вечер": {
        "Описание": "Испеките пиццу или испробуйте новый рецепт.",
        "Идеи": [
            "Создайте пиццу с необычными начинками, каждый может выбрать свои любимые продукты.",
            "Запеките домашние бургеры с различными добавками.",
            "Придумайте тематичное меню, например, итальянскую или японскую кухню."
        ]
    },
    "🍿 Фильм-ночь": {
        "Описание": "Устраивайте вечер просмотра фильмов с закусками.",
        "Идеи": [
            "Выберите несколько фильмов на определенную тему, например, комедии или приключенческие фильмы.",
            "Приготовьте попкорн и закуски, такие как чипсы или пицца.",
            "Сделайте «кинотеатр» в гостиной: надуйте подушки, отключите свет."
        ]
    },
    "🎨 Ручные поделки": {
        "Описание": "Создайте что-нибудь своими руками.",
        "Идеи": [
            "Организуйте сеанс рисования на большом полотне или бумаге.",
            "Сделайте поделки из бумаги, например, оригами или открытки.",
            "Используйте природные материалы для создания украшений или фигурок."
        ]
    },
    "🏡 Пикник дома": {
        "Описание": "Организуйте пикник в гостиной или на балконе.",
        "Идеи": [
            "Приготовьте легкие закуски, такие как сэндвичи, фрукты и соки.",
            "Разложите пледы на полу и создайте атмосферу настоящего пикника.",
            "Устроить игры на свежем воздухе, например, бадминтон или Frisbee на балконе."
        ]
    },
    "📚 Чтение книг": {
        "Описание": "Чтение книг вслух — это увлекательное занятие для всей семьи.",
        "Идеи": [
            "Выберите книгу, интересную для всех членов семьи, и читайте по очереди.",
            "Создайте книгу-сказку, где каждый будет писать свою часть рассказа.",
            "Обсудите прочитанное и поделитесь своими мыслями."
        ]
    },
    "🏃‍♂️ Семейный спорт": {
        "Описание": "Устраивайте спортивные соревнования в доме или на дворе.",
        "Идеи": [
            "Сыграйте в футбол или волейбол на свежем воздухе.",
            "Проведите эстафеты с различными заданиями (скачки, полосы препятствий).",
            "Запланируйте утреннюю зарядку или йогу вместе."
        ]
    },
    "🌈 Украсить дом": {
        "Описание": "Создайте атмосферу праздника, украсив дом.",
        "Идеи": [
            "Используйте гирлянды, шары и рисунки, которые сделаете сами.",
            "Занимайтесь созданием праздничных открыток для родных и друзей.",
            "Устройте конкурсы на лучшее украшение в семье."
        ]
    },
    "🧠 Изучать новое": {
        "Описание": "Выберите тему и изучайте ее вместе.",
        "Идеи": [
            "Запишитесь на онлайн-курсы по интересной теме (язык, кулинария).",
            "Смотрите документальные фильмы и обсудите их.",
            "Устройте вечер викторин на изучаемую тему."
        ]
    },
    "📸 Создание семейного альбома": {
        "Описание": "Соберите семейные фотографии и создайте альбом.",
        "Идеи": [
            "Используйте старые фото и пересказывайте истории, связанные с ними.",
            "Создайте коллажи или тематические страницы.",
            "Добавьте к фото описания и пожелания для каждой отснятой истории."
        ]
    },
    "🧘 Йога или медитация": {
        "Описание": "Проводите время на занятиях йогой или медитацией вместе.",
        "Идеи": [
            "Посмотрите обучающие видео по йоге и следуйте за инструктором.",
            "Устроить вечер расслабляющей медитации со спокойной музыкой.",
            "Обсудите свои ощущения после практики."
        ]
    },
    "🍰 Приготовление десертов": {
        "Описание": "Испеките вместе печенье или торт и украсите их.",
        "Идеи": [
            "Пробуйте разные рецепты и экспериментируйте с начинками.",
            "Устроьте конкурс на лучшее оформление десерта.",
            "Оставьте место для фантазии и создайте собственный рецепт."
        ]
    },
    "🏅 Семейные конкурсы": {
        "Описание": "Устраивайте конкурсы: кто быстрее нарисует, задаст загадку и т.д.",
        "Идеи": [
            "Проведите викторины на общие знания о семье.",
            "Игры, в которых нужно отгадывать слова по картинкам.",
            "Создайте свою версию шоу «Угадай мелодию»."
        ]
    },
    "🎥 Создание видео": {
        "Описание": "Запишите семейное видео или влог о вашем дне.",
        "Идеи": [
            "Постройте сюжет и снимайте его, как в настоящем фильме.",
            "Запишите рецепты и поделитесь своими кулинарными экспериментами.",
            "Создайте видеообзор на любимые игры или игрушки."
        ]
    },
    "🧩 Кроссворды и головоломки": {
        "Описание": "Решайте вместе кроссворды или другие логические задачи.",
        "Идеи": [
            "Составьте собственные кроссворды на темы, интересные вашей семье.",
            "Играйте в логические игры, такие как Судоку или Рубик.",
            "Устройте соревнование на лучшее решение головоломок за время."
        ]
    },
    "🎤 Караоке вечеринка": {
        "Описание": "Устраивайте караоке вечеринку с любимыми песнями всей семьи.",
        "Идеи": [
            "Соберите список любимых песен и пойте их вместе.",
            "Организуйте конкурсы на лучшее исполнение.",
            "Сделайте видеозапись выступления и отправьте родственникам."
        ]
    },
    "🌌 Ночной астрономический сеанс": {
        "Описание": "Проявите интерес к астрономии и наблюдайте за звездами.",
        "Идеи": [
            "Используйте приложения для определения созвездий на ночном небе.",
            "Создайте свой собственный звездный планетарий с помощью бумаги и карандашей.",
            "Проводите время на свежем воздухе, обсуждая факты о планетах и звездах."
        ]
    },
    "🎭 Театральная постановка": {
        "Описание": "Создайте мини-спектакль или инсценировку вместе.",
        "Идеи": [
            "Напишите свою короткую пьесу и распределите роли.",
            "Создайте костюмы и декорации из подручных материалов.",
            "Запишите спектакль на видео и обсудите, как можно улучшить выступление."
        ]
    },
    "🌳 Природные исследования": {
        "Описание": "Проводите время на улице и исследуйте природу.",
        "Идеи": [
            "Соберите коллекцию листьев, ракушек или камней.",
            "Устройте прогулку с задачами по наблюдению за природой.",
            "Организуйте небольшой поход на свежем воздухе с пикником."
        ]
    }
}


def choose_random_activity(activities):
    # Получаем случайный ключ из словаря активностей
    activity_key = random.choice(list(activities.keys()))

    # Получаем описание и идеи для выбранной активности
    activity_info = activities[activity_key]

    # Формируем сообщение с активностью
    message = f"🎉 Выбрана активность: {activity_key} 💫\n\n"
    message += f"📜 Описание: {activity_info['Описание']}\n\n"
    message += "💡 Идеи:\n"

    for idea in activity_info['Идеи']:
        message += f" - {idea}\n"


    return message.strip()  # Удаляем лишние пробелы в конце строки
