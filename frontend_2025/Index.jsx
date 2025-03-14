import stars_background from './assets/stars-background.mp4'
import flaskcon_logo_promo from './assets/flaskcon-2025-logo-promo.png'
import flaskcon_logo_animated from './assets/flaskcon-2025-animated.gif'

export default function Index() {


    return (
        <>
            <section className={"flex flex-col justify-center items-center"}>

                <img src={flaskcon_logo_animated} alt="FlaskCon 2025 Logo."/>

            </section>

            <video autoPlay muted loop id="bg-video">
                <source src={stars_background} type="video/mp4"/>
            </video>
        </>
    )

}
