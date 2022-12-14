from fastapi import APIRouter, Response;
from .lib.factory import Factory;

router = APIRouter();

@router.get('/{repo}/{mod}/next')
async def get_Module(response: Response, repo: str, mod: str, key: str, text: bool = False):
    mgr = Factory.getRepository(repo);
    mod = mgr.getModule(mod);
    
    if mod is not None:
        mod = Factory.fromModule(mod);
        mod.setKey(key);
        mod.increment();

        ret = {
            'Key': mod.getKey(),
            'Text': mod.getText(),
        };

        if not text:
            del ret['Text'];

        return ret;
    
    response.status_code = 404;
    return [];
