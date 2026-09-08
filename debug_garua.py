import asyncio
import os
import zendriver as zd

STATION_URL = (
    "https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/map_red_graf.php"
    "?cod=104079&estado=REAL&tipo_esta=M&cate=CP&cod_old=000208"
)

async def main():
    browser_path = os.environ["GARUA_BROWSER_PATH"]
    config = zd.Config(browser_executable_path=browser_path, sandbox=False)
    browser = await zd.start(config=config)
    page = await browser.get(STATION_URL)

    await asyncio.sleep(10)  # dar tiempo a que cargue/resuelva Cloudflare

    title = await page.evaluate("document.title")
    print("TITULO DE LA PAGINA:", title)

    html = await page.get_content()
    print("LARGO DEL HTML:", len(html))
    print("---- PRIMEROS 2000 CARACTERES ----")
    print(html[:2000])

    await page.save_screenshot("/tmp/senamhi_screenshot.png")
    await browser.stop()

asyncio.run(main())
