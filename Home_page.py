# Python application ~ 7up7down game Home_page.py v2.0
#-----------------------------------------------------------------------------------------------------------------------

# Readme file for more details
# Feel free to use the code
# Mentions and donations will be appreciated
# Reach out via GitHub or Email for any communication
#-----------------------------------------------------------------------------------------------------------------------

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------

from nicegui import ui
from outcome_logic import random_die, player_bet
import httpx


@ui.page('/home_page', title='7up7down')

def home_page():

    ui.audio('Assets/Audio/casino-walk-around_bgm.mp3', autoplay=True).set_visibility(False)

    with ui.image('Assets/Images/casinobanner.jpg').classes('w-full h-screen p-4'):
        with ui.card().classes('fixed-center'):
            ui.image('Assets/Images/casinobannergif.webp').tailwind.border_radius('md')

            with ui.row().classes('items-center justify-center'):
                with ui.card() as sevendown:
                        sevendown.tailwind.background_color('red-700')
                        ui.image('Assets/Images/7num.jpg')
                        ui.icon('arrow_downward').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                        b1 = ui.button('Bet',icon='paid',color='purple-600',on_click = lambda : (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevendown.tailwind.animation('bounce'),b1.props('disable'),player_bet('sevendown'),ui.notify('You bet on 7 down'),b2.props('disable'),b3.props('disable'),rd.props(remove='disable')))
                        b1.tailwind.align_self('center').text_color('orange-300')

                with ui.card() as sevenequal:
                    sevenequal.tailwind.background_color('red-700')
                    ui.image('Assets/Images/7num.jpg')
                    ui.icon('sync_alt').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                    b2 = ui.button('Bet', icon='paid', color='purple-600', on_click=lambda: (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevenequal.tailwind.animation('bounce'),b2.props('disable'), player_bet('sevenequal'),ui.notify('You bet on 7'),b1.props('disable'),b3.props('disable'),rd.props(remove='disable')))
                    b2.tailwind.align_self('center').text_color('orange-300')

                with ui.card() as sevenup:
                    sevenup.tailwind.background_color('red-700')
                    ui.image('Assets/Images/7num.jpg')
                    ui.icon('arrow_upward').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                    b3 = ui.button('Bet', icon='paid', color='purple-600', on_click=lambda: (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevenup.tailwind.animation('bounce'),b3.props('disable'), player_bet('sevenup'),ui.notify('You bet on 7 up'),b1.props('disable'),b2.props('disable'),rd.props(remove='disable')))
                    b3.tailwind.align_self('center').text_color('orange-300')

            rd = ui.button('Roll dice',color='purple-600',icon='casino',on_click = lambda :(random_die(),playagain(),rd.props('disable'),sevendown.tailwind.animation('none'),sevenup.tailwind.animation('none'),sevenequal.tailwind.animation('none'))).props('disable')

            rd.tailwind.align_self('center').text_color('orange-300')

    with ui.footer().classes('bg-white text-black justify-start items-center'):

        ui.label('Designed and developed by kaushal.shastry@outlook.com © 2026').style('font-family: "Roboto"')

        with ui.row():
            with ui.link(target='https://www.linkedin.com/in/kaushal-shastry/', new_tab=True):
                ui.image('Assets/Images/linkedin.png').classes('w-8')

            with ui.link(target='https://www.youtube.com/@kaushalshastry6973', new_tab=True):
                ui.image('Assets/Images/youtube.png').classes('w-8')

            with ui.link(target='https://github.com/kaushal1904/projects', new_tab=True):
                ui.image('Assets/Images/github.png').classes('w-8')

        ui.space()

        ui.label('Built for big screens').classes('justify-end')

        def playagain():
            pa = ui.button('Play again!', icon='sync', color='purple-600',
                                    on_click=lambda: ui.navigate.to('home_page'))
            pa.tailwind.align_self('center').text_color('orange-300')
    ui.run(favicon='Assets/Images/7num_favicon.png')

home_page()


@ui.page('/health',title='Health check - 7up7down')
async def health():
    async with httpx.AsyncClient() as client:
        response =  await client.get('https://sevenup7down-v1.onrender.com/')
        print(response.status_code)

        if response.status_code==200:
            ui.label('Server up and running')

        else:
            ui.label(f'Server down with status code: {response.status_code}')






