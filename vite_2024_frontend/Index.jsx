import flaskcon_logo from './assets/flaskcon-2024-animated.gif'
import bottom_clouds from './assets/bottom-clouds.png'
import {createSignal, onMount} from "solid-js";

export default function Index() {

    const [loggedIn, setLoggedIn] = createSignal(false)

    const dev = import.meta.env.DEV
    const api = dev ? 'http://localhost:5000/' : '/'

    function isLoggedIn() {
        fetch(api + '2024/api/logged-in', {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.logged_in) {
                    setLoggedIn(true)
                }
            })
    }

    onMount(() => {
        isLoggedIn()
    })

    return (
        <section>
            <div className={'hero'}>
                <div className={'hero-overlay'} style={{background: `url(${bottom_clouds}) repeat-x bottom`}}>
                    <img src={flaskcon_logo} alt="FlaskCon 2024 Logo."/>
                </div>
            </div>
            <section className={'container'}>
                <h1 className={'text-center my-14'}>
                    FlaskCon 2024 will be happening Friday, May 17 inside PyCon US 2024.
                </h1>
            </section>
            <section className={'container mb-14'}>
                <h2 className={'text-center m-5'}>Call for proposals are now live!</h2>

                <div className={'flex justify-center w-full'}>

                    {
                        loggedIn() ?
                            <div className={'flex flex-col gap-2 text-center'}>
                                <a className={'btn'} href={'https://flaskcon.com/account'}>Go to my account</a>
                            </div>
                            :
                            <div className={'flex flex-col gap-2 text-center'}>
                                <a className={'btn'} href={'https://flaskcon.com/signup'}>Signup To Join In</a>
                                <a href={'https://flaskcon.com/login'}>...or login here</a>
                            </div>
                    }
                </div>
            </section>
            <section className={'container'}>
                <h2 className={'my-5'}>Speaking Experience</h2>
                <ul>
                    <li>We are focused on accepting lightning talks this year, typically 5 - 15 mins.</li>
                    <li>If your talk is selected, you'll be invited to attend FlaskCon which will be held
                        inside PyCon US (Pittsburgh, Pennsylvania, USA)
                    </li>
                </ul>
            </section>

            <section className={'container'}>
                <h2 className={'my-5'}>The Current Schedule (may change)</h2>
                <table>
                    <thead>
                    <tr>
                        <th>Time</th>
                        <th>Event</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>11:00 - 11:15</td>
                        <td>Intro from David Lord</td>
                    </tr>
                    <tr>
                        <td>11:15 - 11:40</td>
                        <td>State of Pallets</td>
                    </tr>
                    <tr>
                        <td>11:40 - 12:00</td>
                        <td>Q&A</td>
                    </tr>
                    <tr>
                        <td>12:00 - 13:00</td>
                        <td>Lightning Talks</td>
                    </tr>
                    <tr>
                        <td>13:00 - 14:00</td>
                        <td>Lunch</td>
                    </tr>
                    <tr>
                        <td>14:00 - 14:25</td>
                        <td>Being a Better Community</td>
                    </tr>
                    <tr>
                        <td>14:30 - 15:30</td>
                        <td>Lightning Talks</td>
                    </tr>
                    <tr>
                        <td>15:40 - 16:00</td>
                        <td>Becoming a Contributor</td>
                    </tr>
                    <tr>
                        <td>16:00 - 16:30</td>
                        <td>Break</td>
                    </tr>
                    <tr>
                        <td>16:30 - 17:30</td>
                        <td>Lightning Talks</td>
                    </tr>
                    <tr>
                        <td>17:30 - 17:40</td>
                        <td>Future of Pallets</td>
                    </tr>
                    <tr>
                        <td>17:40 - 18:00</td>
                        <td>Panel Q&A</td>
                    </tr>
                    <tr>
                        <td>18:00 - 19:00</td>
                        <td>General Mixer?</td>
                    </tr>
                    </tbody>
                </table>
            </section>
            <section className={'container text-center'}>
                <p className={'text-sm'}>Copyright &copy; 2024 FlaskCon, A PSF-registered trademark owned by
                    Pallets.</p>
            </section>
        </section>

    )

}