import Sidebar from "./components/Sidebar"
import Page from "./layout/Page"

function Home() {

  return (
    <div className="flex">
        <Sidebar />
        <Page>
          <h1 className="text-3xl font-bold">
              suivi - Home
          </h1>
        </Page>
    </div>
  )
}

export default Home
