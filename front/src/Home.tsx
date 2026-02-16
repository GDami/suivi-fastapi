import PageTitle from "./components/PageTitle"
import Sidebar from "./components/Sidebar"
import Page from "./layout/Page"

function Home() {

  return (
    <div className="flex">
        <Sidebar />
        <Page>
          <PageTitle>
              suivi - Accueil
          </PageTitle>
        </Page>
    </div>
  )
}

export default Home
