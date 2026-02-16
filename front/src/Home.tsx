import PageTitle from "./components/PageTitle"
import Sidebar from "./components/Sidebar"
import Page from "./layout/Page"

function Home() {

  return (
    <div className="flex">
        <Sidebar />
        <Page>
          <PageTitle>
              suivi - Home
          </PageTitle>
        </Page>
    </div>
  )
}

export default Home
