import flaskcon_logo_promo from './assets/flaskcon-2025-logo-promo.png'
import stars_background from "./assets/stars-background.mp4";

export default function ComingSoon() {

    return (
        <>
            <section className={"flex flex-col justify-center items-center h-screen"}>

                <img src={flaskcon_logo_promo} alt="FlaskCon 2024 Logo."/>

                <h1>Coming Soon!</h1>

            </section>

            <video autoplay muted loop id="bg-video">
                <source src={stars_background} type="video/mp4"/>
            </video>
        </>
    )

}