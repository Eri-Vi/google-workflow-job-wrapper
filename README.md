# Job Wrapper in Google Workflows

Lightweight orchestration wrapper for a job (e.g. Dataflow).
- Allows conditional retrying of the job when it crashes, fails, times out.
- Entirely serveress and easiliy configured with a YAML file.
- Only modification required to the job is a success/failure call to the callback URL.

## Testing the PoC

This PoC demos 3 cases: job success, job requesting a retry, and job timeout.

To test each, trigger the Workflow with the payload:

```json
{
    "status": "(ok|retry|timeout)"
}
```
