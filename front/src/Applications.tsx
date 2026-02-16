import ApplicationList from "./components/ApplicationList"
import PageTitle from "./components/PageTitle"
import Sidebar from "./components/Sidebar"
import Page from "./layout/Page"

function Applications() {

  return (
    <div className="flex">
        <Sidebar />
        <Page>
          <PageTitle>
              suivi - Candidatures
          </PageTitle>
          <ApplicationList />
        </Page>
    </div>
  )
}

export default Applications
