import stars_background from './assets/stars-background.mp4'
import flaskcon_logo_animated from './assets/flaskcon-2025-stars.gif'
import pycon_2025_logo from './assets/pyconus-logo-e.svg'

export default function Index() {


    return (
        <>
            <video autoPlay muted loop id="bg-video">

                <source src={stars_background} type="video/mp4"/>

            </video>
            <main>
                <div className={"container"}>
                    <section className={"logo-container"}>

                        <img src={flaskcon_logo_animated} alt="FlaskCon 2025 Logo."/>
                        <img src={pycon_2025_logo} className={"pyconus-logo"} alt="pycon2025 Logo."/>

                    </section>

                    <section className={"text-center p-5"}>
                        <h1>Friday May 16, 2 PM -6 PM</h1>
                        <p className={"my-2"}>Inside PyCon US</p>
                    </section>

                    <section className={"text-center p-2"}>
                        <p>Join us in a mini conference dedicated to Flask,
                            its community and ecosystem, as well as related
                            web technologies. Meet maintainers and community
                            members, learn about how to get involved,
                            and join us during the sprint days to contribute.
                            Submit your talk proposal today!</p>

                        <a className={"a-button my-10"}
                           href={"https://www.papercall.io/flaskcon-pyconus2025"}>

                            Submit a talk

                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"
                                 fill="none"
                                 stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                 className="lucide lucide-square-arrow-out-up-right">
                                <path d="M21 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h6"/>
                                <path d="m21 3-9 9"/>
                                <path d="M15 3h6v6"/>
                            </svg>

                        </a>

                        <p>
                            CFP closes at April 24, 2025 00:00 UTC
                        </p>

                    </section>


                    <footer className={"text-center text-xs py-20"}>
                        Copyright © 2024 FlaskCon, A PSF-registered trademark owned by Pallets.
                    </footer>
                </div>
            </main>

        </>
    )

}
