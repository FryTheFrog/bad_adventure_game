welcome_ui = """
WELCOME !
Usually you'll see something like this:
|              INFO               | -> usually shows your location
|---------------------------------|
|                                 |
|             INFO                | -> shows a nice ACII-Artwork
|               or                |    or a menu
|               ART               |
|                                 |
|---------------------------------|
|  action  |  action  |  action   | -> shows the actions you may do
|   char   |   char   |   char    | -> shows the char you have to enter 

   => enter the char under the action you want to perform
      into the console after " >  " and press "Enter"

   => enter any char to continue
> """

village_ui = """
|               Village               |             Leave              |
|-------------------------------------|--------------------------------|
|                                     |       v .   ._, |_  .,         |
|  ~         ~~          __           |    `-._\/  .  \ /    |/_ .-    |
|         _T      .,,.    ~--~ ^^     |        |\  _\, y | \//         |
|   ^^   // \                    ~    |  _\_.___|\, \|/ -.\||          |
|        ][O]    ^^      ,-~ ~        |    `7-,--.`._||  / / ,         |
|     /''-I_I         _II____         |    /'     `-. `./ / |/_.'      |
|  __/_  /   \ ______/ ''   /'\_,__   |        ..    |    |//     ,    |
|    | II--'''' \,--:--..,_/,.-{ },   |              |_    /      -~   |
|  ; '/__\,.--';|   |[] .-.| O{ _ }   |              |-   |            |
|  :' |  | []  -|   ''--:.;[,.'\,/    |     .v^'     |   =|            |
|  '  |[]|,.--'' '',   ''-,.    |     |     v|]y     |    |            |
|    ..    ..-''    ;       ''. '     | ----/`|-----/ ,  . \--------._ |
|-------------------------------------|--------------------------------|
| weapon smith | hotel | notice board | witch hut | explore the forest |
|      1       |   2   |      3       |     4     |         5          |
> """

smith_ui = """
|                             Weaponsmith                              |
|----------------------------------------------------------------------|
|                                                                      |
|          />_________________________________          A          .   |
| [########[]_________________________________>        /!\             |
|          \>                                         / ! \            |
|                          ___  ,O.            /\     )___(            |
|         -~   \,          ',  ----,          (  `.____(_)_________    |
|              ,                              |           __..--""     |
|  ..            )                            (       _.-|             |
|               (_)                            \    ,' | |             |
|               |`|                ,            \  /   | |         O   |
|               | |  _()         ___ O_  -       \(    | |      ..     |
|             \_|_|_/         .   0   --,         `    | |             |
|----------------------------------------------------------------------|
| open inventory |     buy item     |    sell item    |      back      |
|       i        |        b         |        s        |       q        |
> """

witch_ui = """
|                              Witch Hut                               |
|----------------------------------------------------------------------|
|                               (_)                    /\              |
|                       ________[_]________           /  \  /\         |
|              /\      /\        ______    \       /\/    \/  \        |
|             /  \    //_\       \    /\    \     /   /\/\  /\/\       |
|      /\    / /\/\  //___\       \__/  \    \   /\/\/    \/    \      |
|     /  \  /\/    \//_____\       \ |[]|     \ /                      |
|    /\/\/\/       //_______\       \|__|      \                       |
|   /      \      /XXXXXXXXXX\                  \                      |
|           \    /_I_II  I__I_\__________________\                     |
|                  I_I|  I__I_____[]_|_[]_____I                        |
|                  I_II  I__I_____[]_|_[]_____I                        |
|                  I II__I  I     XXXXXXX     I                        |
|----------------------------------------------------------------------|
| open inventory |     buy item     |    sell item    |      back      |
|       i        |        b         |        s        |       q        |
> """

board_ui = """

          ___________________________________________________
         |                  ~ Notice Board ~                 |
        |-----------------------------------------------------|
        |                                                     |
        |                     BOUNTY HUNT                     |
        |                                                     |
        |               999 coins will be payed               |
        |                  to the slayer of:                  |
        |                     ENEMY NAME                      |
        |                                                     |
        |                  difficulty: hard                   |
        |-----------------------------------------------------|
        | |                                                 | |
        | |                      Close                      | |
.---.--/   \----.---.---.-..--.-   q   .---.-.-.----...-.--/   \---.-..

> """

hotel_ui = """
|                                Hotel                                 |
|----------------------------------------------------------------------|
|                       -_--                       ____                |
|   ____                             - -                               |
|         -------   __                                                 |
|                                           ;,'            _.._..,_,_  |
|                                   _o_    ;:;'           (          ) |
|                               ,-.'---`.__ ;              ]~,"-.-~~[  |
|     ;)( ;                    ((j`=====',-'             .=])' (;  ([  |
|    :----:     o8Oo./          `-\     /                | ]:: '    [  |
|   C|====| ._o8o8o8Oo_.           `-=-'     ----        '=]): .)  ([  |
|    |    |  \========/   --                               |:: '    |  |
|    `----'   `------'      ____            ---             ~~----~~   |
|   ___                                                                |
|----------------------------------------------------------------------|
| open inventory |            take a break            |      back      |
|       i        |                 x                  |       q        |
> """

forest_ui = """
|                              The Forest                              |
|----------------------------------------------------------------------|
|   .                                              v .   ._, |_  .,    |
|             .      *        *                 `-._\/  .  \ /    |/_ .|
|        .                 .                        |\  _\, y | \//    |
|         _    .  ,   .           .           _\_.___|\, \|/ -.\||     |
|     *  / \_ *  / \_      _  *        *   /\ __`7-,--.`._||  / / ,    |
|       /    \  /    \,   ((        .    _/  /  /'     `-. `./ / |/_.' |  
|  .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.     |    |//     |
|     /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  * |_    /      |
|   /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \  |-   |       |
|  /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-   |   =|       |
| /        `.  / /       `.~-^=-=~=^=.-'      '-._ `._    |    |       |
|                                                        / ,  . \      |
|----------------------------------------------------------------------|
| open inventory |       hunt       |     collect     |      back      |
|       i        |        h         |        c        |       q        |
> """

combat_ui = """
|                              ENEMY NAME                              |
|----------------------------------------------------------------------|
|                                           `:.`---.__         `-._    |
|                                             `:.     `--.         `.  |
|             +       |                         \.        `.         `.|
|             |  \+/  |                 (,,(,    \.         `.   ____,-|
|             | _<=>_ |              (,'     `/   \.   ,--.___`.'      |
|             0/ \ / o=o         ,  ,'  ,--.  `,   \.;'         `      |
|             \/\ ^ /`0           `{D, {    \  :    \;                 |
|             | /_^_\               V,,'    /  /    //                 |
|             | || ||               j;;    /  ,' ,-//.    ,---.      , |
|           __|_d|_|b__             \;'   /  ,' /  _  \  /  _  \   ,'/ |
| Energy | ████████████████████    |      \   `'  / \  `'  / \  `.' /  |
| Health | █████████████████       |      ██████████████████ | Health  |
|----------------------------------------------------------------------|
| open inventory |               attack               |      flee      |
|       i        |                 a                  |       q        |
> """

inventory_ui = """
|                              Inventory                | Gold: 999999 |
|----------------------------------------------------------------------|
| 01x Beskar Sword      | value per unit: 200  | equipped              |
| effect(s): grants bonus damage of 40                                 |
|----------------------------------------------------------------------|
| 01x Beskar Armor      | value per unit: 250  | equippable            |
| effect(s): grants bonus armor of 70                                  |
|----------------------------------------------------------------------|
| consume item          | (un)equip item              |      back      |
| enter name of item you want to (un)equip or consume |       q        |
> """

buy_ui = """
|                                 Shop                  | Gold: 999999 |
|----------------------------------------------------------------------|
| 01x Beskar Sword      | value per unit: 200  | equippable            |
| effect(s): grants bonus damage of 40                                 |
|----------------------------------------------------------------------|
| 01x Beskar Armor      | value per unit: 250  | equippable            |
| effect(s): grants bonus armor of 70                                  |
|----------------------------------------------------------------------|
|             enter the NAME of the item              |      back      |
|                   you want to BUY                   |       q        |
> """

sell_ui = """
|                                 Shop                  | Gold: 999999 |
|----------------------------------------------------------------------|
| 01x Beskar Sword      | value per unit: 200  | equipped              |
| effect(s): grants bonus damage of 40                                 |
|----------------------------------------------------------------------|
| 01x Beskar Armor      | value per unit: 250  | equippable            |
| effect(s): grants bonus armor of 70                                  |
|----------------------------------------------------------------------|
| You may only sell items that are not equipped !     |      back      |
| enter NAME of item you want to SELL                 |       q        |
> """

message_ui = """

         -----------------------------------------------------
        |                      ATTENTION                      |
        |-----------------------------------------------------|
        | --------------------------------------------------- |
        |                                                     |
        | {} |
        | {} |
        | {} |
        | {} |
        |                                                     |
        | --------------------------------------------------- |
        |-----------------------------------------------------|
        |                        Close                        |
        |                          q                          |
         -----------------------------------------------------

> """

death_ui = """
|                               You Died                               |
|----------------------------------------------------------------------|
|                                ______                                |
|                             .-"      "-.                             |
|                            /            \                            |
|                           |              |                           |
|                           |,  .-.  .-.  ,|                           |
|                           | )(__/  \__)( |                           |
|                           |/     /\     \|                           |
|                           (_     ^^     _)                           |
|                            \__|IIIIII|__/                            |
|                             | \IIIIII/ |                             |
|                             \          /                             |
|                              `--------`                              |
|----------------------------------------------------------------------|
|             Restart               |               Quit               |
|                r                  |                x                 |
> """
