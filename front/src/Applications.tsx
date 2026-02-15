import Sidebar from "./components/Sidebar"
import Page from "./layout/Page"

function Applications() {

  return (
    <div className="flex">
        <Sidebar />
        <Page>
          <h1 className="text-3xl font-bold">
              suivi - Applications
          </h1>
        </Page>
    </div>
  )
}

export default Applications
