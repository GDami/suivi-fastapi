import { AddButton } from "./components/AddButton"
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
			<div className="p-4">
				<AddButton
					text="Ajouter une candidature"
				/>
			</div>
          <ApplicationList />
        </Page>
    </div>
  )
}

export default Applications
