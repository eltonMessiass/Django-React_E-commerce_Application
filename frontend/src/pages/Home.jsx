import React from 'react'
import Header from '../components/Header'

function Home() {
  return (
    <div>
        <Header/>
      <div className='text-center items-center flex flex-col gap-4'>
        <span className='text-9xl font-normal'>Intelligence</span>
        <p className='text-5xl'>IA para todos nós</p>
        <div className='m-2 w-32 h-11 text-white text-xl bg-blue-600 border-2 rounded-full flex items-center justify-center'>
            <a href="#">Saiba mais</a>
        </div>
      </div>
      <div className='w-full  mb-5'>
        <video autoPlay loop muted className='w-full h-[50rem]'>
            <source src='https://www.apple.com/105/media/us/mac/family/2024/60fc0159-4236-4a03-8534-f5ba07e538c5/anim/welcome/xlarge.mp4' type='video/mp4' />
            Seu navegador não suporta a tag de vídeo.
        </video>
      </div>

      <div className='w-full h-[50rem] mb-7 text-center bg-black text-white'>
        <span className='text-6xl'>iPhone 15 Pro</span>
        <p>Titânio. Muito robusto. Muito leve. Muito Pro.</p>
        <div className='flex flex-col gap-3 w-full items-center justify-center'>
            <div className='flex flex-row'>
                <div className='m-2 w-32 h-11 text-white text-xl bg-blue-600 border-2 rounded-full flex items-center justify-center'>
                    <a href="#">Saiba mais</a>
                </div>
                <div className='m-2 w-32 h-11 text-white text-xl bg-blue-600 border-2 rounded-full flex items-center justify-center'>
                    <a href="#">Comprar</a>
                </div>
            </div>

            <img className='h-[40rem] ' src="https://www.lux.camera/content/images/size/w2000/2023/10/hero-4.jpg" alt="iphone15" />
        </div>

      </div>
    </div>
  )
}

export default Home
