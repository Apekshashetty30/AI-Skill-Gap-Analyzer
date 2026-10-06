import { useEffect, useState } from 'react'
import './App.css'

function App() {
 const [jobs, setJobs] = useState([])
const [selectedJob, setSelectedJob] = useState('')
const [result, setResult] = useState(null)
const [resumeFile, setResumeFile] = useState(null)
const [resumeId, setResumeId] = useState(1)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/jobs/')
      .then((response) => response.json())
      .then((data) => setJobs(data))
      .catch((error) => console.error('Error:', error))
  }, [])
const uploadResume = () => {
  if (!resumeFile) {
    alert('Please select a resume')
    return
  }

  const formData = new FormData()
  formData.append('resume', resumeFile)

  fetch('http://127.0.0.1:8000/api/upload-resume/', {
    method: 'POST',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      setResumeId(data.resume_id)
      alert('Resume uploaded successfully')
    })
    .catch((error) => console.error('Error:', error))
}
  const analyzeSkillGap = () => {
    if (!selectedJob) {
      alert('Please select a job')
      return
    }

   fetch(`http://127.0.0.1:8000/api/skill-gap/${selectedJob}/${resumeId}/`)
      .then((response) => response.json())
      .then((data) => setResult(data))
      .catch((error) => console.error('Error:', error))
  }

  return (
    <div className="app">
      <h1>AI Skill Gap Analyzer</h1>

      <p>Find the skills you have and the skills you need.</p>

      <div className="card">
        <label>Upload Resume:</label>

<input
  type="file"
  accept=".pdf,.doc,.docx,.txt"
  onChange={(e) => setResumeFile(e.target.files[0])}
/>
<button onClick={uploadResume}>
  Upload Resume
</button>
        <label>Select Job:</label>

        <select
          value={selectedJob}
          onChange={(e) => setSelectedJob(e.target.value)}
        >
          <option value="">-- Select a Job --</option>

          {jobs.map((job) => (
            <option key={job.id} value={job.id}>
              {job.job_title}
            </option>
          ))}
        </select>

        <button onClick={analyzeSkillGap}>
          Analyze Skill Gap
        </button>
      </div>

      {result && (
        <div className="result">
          <h2>Skill Gap Result</h2>

          <h3>Required Skills</h3>
          <p>{result.required_skills.join(', ')}</p>

          <h3>Available Skills</h3>
          <p>{result.available_skills.join(', ')}</p>

          <h3>Missing Skills</h3>
          <p>{result.missing_skills.join(', ')}</p>

          <h2>Skill Gap: {result.skill_gap_percentage}%</h2>
        </div>
      )}
    </div>
  )
}

export default App