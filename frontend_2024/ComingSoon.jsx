import flaskcon_logo from './assets/flaskcon-2024-animated.gif'
import bottom_clouds from './assets/bottom-clouds.png'

export default function ComingSoon() {

    return (
        <section>
            <div className={'hero'}>
                <div className={'hero-overlay'} style={{background: `url(${bottom_clouds}) repeat-x bottom`}}>
                    <img src={flaskcon_logo} alt="FlaskCon 2024 Logo."/>
                </div>
            </div>
            <section className={'container text-center '}>
                <h1 className={'my-14'}>
                    Coming Soon!
                </h1>
                <p>Check back here for more details!</p>
            </section>
        </section>
    )

}