pipeline {
    agent {
        label 'master'
    }
    stages {
        stage('CSV to RDF') {
            agent {
                docker {
                    image 'cloudfluff/databaker'
                    reuseNode true
                }
            }
            steps {
                sh "python to_ttl.py > cn8-hmrc.ttl"
            }
        }
        stage('Upload') {
            steps {
                script {
                    def pmd = pmdConfig('pmd')
                    def draftset = pmd.drafter.listDraftsets().find { it['display-name'] == env.JOB_NAME }
                    if (draftset) {
                        pmd.drafter.deleteDraftset(draftset.id)
                    }
                    def id = pmd.drafter.createDraftset(env.JOB_NAME).id
                    String graph = "http://gss-data.org.uk/graph/cn8-hmrc"
                    pmd.drafter.deleteGraph(id, graph)
                    pmd.drafter.addData(id, "${WORKSPACE}/cn8-hmrc.ttl", "text/turtle", "UTF-8", graph)
                    pmd.drafter.publishDraftset(id)
                }
            }
        }
    }
    post {
        success {
            build job: '../GDP-tests', wait: false
        }
    }
}
